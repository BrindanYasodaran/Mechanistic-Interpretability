import os
import torch as t
import torch.distributed as dist
import torch.multiprocessing as mp

WORLD_SIZE = t.cuda.device_count()

os.environ["MASTER_ADDR"] = "localhost"
os.environ["MASTER_PORT"] = "12345"


def send_receive(rank, world_size):
    dist.init_process_group(backend="gloo", rank=rank, world_size=world_size)

    if rank == 0:
        sending_tensor = t.zeros(1)
        print(f"{rank=}, sending {sending_tensor=}")
        dist.send(tensor=sending_tensor, dst=1)
    elif rank == 1:
        received_tensor = t.ones(1)
        print(f"{rank=}, creating {received_tensor=}")
        dist.recv(received_tensor, src=0)
        print(f"{rank=}, received {received_tensor=}")

    dist.destroy_process_group()


if __name__ == "__main__":
    world_size = 2
    mp.spawn(send_receive, args=(world_size,), nprocs=world_size, join=True)
