from objects import Product, Book, Movie, Album, Media

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()

def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
    if isinstance(product, Media):  # Check if the product is a Media object
        print(f"{'Format:':{w}}{product.format}")  # Display the format
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

def main():
    print("The Product Viewer program")
    print()
    
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Michael Lewis", "Hardcover"),  # Store "Hardcover" as the format
                Movie("Inception", 19.95, 8, 2010, "DVD"),  # Store "DVD" as the format
                Album("The Dark Side of the Moon", 10.99, 15, "Pink Floyd", "Vinyl"))  # New Album object
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        number = int(input("Enter product number: "))
        print()

        product = products[number-1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
