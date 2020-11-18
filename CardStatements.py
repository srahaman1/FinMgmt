def attempt1():
    import PyPDF2 as p2

    """Attempting to extract the data straight from Monthly Credit Card Statements, later learned how to directly download a csv file of transactions from Chase.com"""
    File = open(
        "C:/Users/srahaman1/Documents/Money Management/Chase_Sept_2020.pdf", "rb"
    )
    statement = p2.PdfFileReader(File)

    if statement.isEncrypted:
        statement.decrypt("")
        print(statement.getNumPages())

    """Extract Single Page, 2nd page of Chase Statement"""
    bill1 = statement.getPage(2)
    bill1 = bill1.extractText()
    # print(type(bill1))
    # print(bill1)
    start = bill1.index("Payment Thank You")
    end = bill1.index("Total fees charged")
    purchases = bill1[start + 37 : end]

    lines = []
    for line in purchases:
        transaction = purchases[0 : purchases.index("\n")]
        lines.append(transaction)
        purchases -= transaction

    pass


# Bank 1
import pandas as pd

"""Convert txt file to usable csv file"""
read_file = pd.read_csv(
    r"C:/Users/srahaman1/Documents/Money Management/FBC_Sept_2020.txt", header=None
)
read_file.columns = ["Transaction Date", "Amount", "Description"]
read_file.to_csv(
    r"C:/Users/srahaman1/Documents/Money Management/FBC_Sept_2020.csv", index=None
)
