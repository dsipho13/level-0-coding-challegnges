def triangle_area(side1, side2, side3):
    semiparam = (side1 + side2 + side3) / 2
    area = (
        semiparam * (semiparam - side1) * (semiparam - side2) * (semiparam - side3)
    ) ** (
        0.5
    )  # Heron's formula
    return area


def main():
    print(triangle_area(3, 3, 3))


if __name__ == "__main__":
    main()
