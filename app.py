import click
from faker import Faker
from tqdm import tqdm
from database import Database


def random_generate_data(db, count=100):
    f = Faker(["zh_CN"])
    for i in tqdm(range(count)):
        db.set(f.uuid4(), f.street_name())

    db.commit()


@click.command()
@click.option("--method", default="get", help="set or get")
@click.option("--key", prompt="key")
@click.option("--value")
def main(method="get", key="", value=None):
    db = Database()
    try:
        # random_generate_data(db)
        # return
        if method == "set":
            db.set(key, value, commit=True)
        ret = db.get(key)
        click.echo(ret)
    except:
        pass
    finally:
        db.close()


if __name__ == "__main__":
    main()