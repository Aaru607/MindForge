import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database.seed_data import DatabaseSeeder

async def main():
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    
    seeder = DatabaseSeeder(mongo_uri)
    await seeder.seed_all()
    
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
