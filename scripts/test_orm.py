from backend.config.database import SessionLocal
from backend.models.company import Company


def main():
    session = SessionLocal()

    companies = session.query(Company).all()

    print(f"Total Companies: {len(companies)}")

    for company in companies:
        print(
            company.company_id,
            company.company_name,
            company.industry
        )

    session.close()


if __name__ == "__main__":
    main()