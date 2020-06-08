from .tasks import render

def main():
    render.delay()

if __name__ == "__main__":
    main()