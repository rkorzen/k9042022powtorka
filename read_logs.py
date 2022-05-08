
import sys 

in_file = sys.argv[1]
out_file = sys.argv[2]

print(f"in: {in_file}, out: {out_file}")


def main():
    with open(in_file) as logs:
        for line in logs:
            print(line)
    
    
    
if __name__ == "__main__":
    main()
