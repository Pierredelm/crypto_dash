import sys


def calculate_vat(price_ht: float, vat_rate: float = 0.20) -> float:
    """Calculates the VAT amount for a given price."""
    return price_ht * vat_rate


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates the final price after applying a discount percentage."""
    if discount_percent < 0:
        raise ValueError("Discount percent must be positive.")
    if discount_percent > 100:
        raise ValueError("Discount percent must be less than 100.")        
    return price * (1 - discount_percent / 100)
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            input_price = float(sys.argv[1])
            input_discount = float(sys.argv[2])
            final_price = calculate_discount(input_price, input_discount)
            print(
                f"Original Price: ${input_price:.2f} | Discount: {input_discount}% -> Final Price: ${final_price:.2f}"
            )
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Usage: python commerce_utils.py <price> <discount_percent>")
        print("Example: python commerce_utils.py 50 13")    
