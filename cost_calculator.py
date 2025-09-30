# AWS Cloud Cost Calculator

def ec2_cost(hours, rate=0.023):  # default: t2.micro in US-East
    return hours * rate

def s3_cost(storage_gb, rate=0.023):  # default: $0.023 per GB
    return storage_gb * rate

def main():
    print("=== AWS Cloud Cost Calculator ===")

    # Get user inputs
    hours = float(input("Enter EC2 usage hours: "))
    storage = float(input("Enter S3 storage in GB: "))

    # Calculate costs
    ec2 = ec2_cost(hours)
    s3 = s3_cost(storage)
    total = ec2 + s3

    # Show results
    print(f"\nEstimated EC2 cost: ${ec2:.2f}")
    print(f"Estimated S3 cost: ${s3:.2f}")
    print(f"Total estimated monthly cost: ${total:.2f}")

if __name__ == "__main__":
    main()
