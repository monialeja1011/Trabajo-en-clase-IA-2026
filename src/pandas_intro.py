import pandas as pd

def main():
    df = pd.read_csv("data/cultivos_detalle.csv")

    print("\n=== Primer vistazo al DataFrame ===")
    print(df.head())

    print("\n=== Información del DataFrame ===")
    print(df.info())

    print("\n=== Estadísticas descriptivas ===")
    print(df.describe())

if __name__ == "__main__":
    main()
