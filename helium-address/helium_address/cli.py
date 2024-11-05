import argparse
from .address import Address

def main():
    parser = argparse.ArgumentParser(description='Convert between Helium address formats')
    parser.add_argument('address', help='Address to convert')
    parser.add_argument('-v', '--verbose', action='store_true', 
                      help='Show both base58 and base64 representations')
    
    # Use mutually exclusive group to ensure only one --from flag is used
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--from-b58', action='store_true',
                      help='Input address is in base58 format')
    group.add_argument('--from-b64', action='store_true',
                      help='Input address is in base64 format (default)')
    
    args = parser.parse_args()
    
    try:
        # Create Address object from input
        if args.from_b58:
            address = Address.fromB58(args.address)
        else:  # default to base64
            address = Address.fromB64(args.address)
            
        if args.verbose:
            print(f"Base64:  {address.b64}")
            print(f"Base58:  {address.b58}")
        else:
            # Print the opposite format of what was input
            print(address.b64 if args.from_b58 else address.b58)
            
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
