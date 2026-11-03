from dataclasses import dataclass
from datetime import date


@dataclass
class Item:
    description: str
    quantity: int
    unit_price: float

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price


def build_invoice(client: str, items: list[Item], tax_rate: float = 0.18) -> str:
    subtotal = sum(i.total for i in items)
    tax = subtotal * tax_rate
    lines = [
        f"INVOICE  |  Date: {date.today():%d %b %Y}",
        f"Billed to: {client}",
        "-" * 50,
        f"{'Description':<25}{'Qty':>5}{'Price':>9}{'Total':>11}",
    ]
    for i in items:
        lines.append(f"{i.description:<25}{i.quantity:>5}{i.unit_price:>9.2f}{i.total:>11.2f}")
    lines += [
        "-" * 50,
        f"{'Subtotal':<39}{subtotal:>11.2f}",
        f"{f'Tax ({tax_rate:.0%})':<39}{tax:>11.2f}",
        f"{'TOTAL':<39}{subtotal + tax:>11.2f}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    items = [Item("Web design", 1, 15000), Item("Hosting (months)", 12, 500)]
    print(build_invoice("Acme Pvt Ltd", items))