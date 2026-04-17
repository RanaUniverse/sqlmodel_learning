from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


engine = create_engine(
    url=sqlite_url,
    echo=True,
)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive wilson the bosy")
    hero_2 = Hero(name="spider boy", secret_name="Pedro paraueido")
    hero_3 = Hero(name="Rusty Man", secret_name="TOmmy sharp", age=48)

    session = Session(bind=engine)

    # session.add(hero_1)
    # session.add(hero_2)
    # session.add(hero_3)
    # session.commit()
    # session.close()

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        print("After adding to the session:")
        print("Hero 1", hero_1)
        print("Hero 2", hero_2)
        print("Hero 3", hero_3)
        session.commit()
        session.refresh(hero_1)
        session.refresh(hero_2)
        session.refresh(hero_3)
        print("After adding to the commit fully:")
        print("Hero 1", hero_1)
        print("Hero 2", hero_2)
        print("Hero 3", hero_3)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()
