import asyncio
import random


async def download_file(file_name: str, duration: int):
    print(f"Start downloading {file_name}")
    await asyncio.sleep(duration)
    print(f"Finished downloading {file_name} in {duration} seconds")


async def main():
    files = [(f"file_{i}.txt", random.randint(1, 5)) for i in range(1, 6)]
    tasks = [download_file(file, duration) for file, duration in files]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
