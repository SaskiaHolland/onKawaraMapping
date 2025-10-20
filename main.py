from src import map_oper
from src.utils import OUTPUT_DIR, OUTPUT_FILE

if __name__ == "__main__":
    kawaraMap = map_oper.creating_map()

    OUTPUT_DIR.mkdir(exist_ok=True)

    kawaraMap.save(str(OUTPUT_FILE))
