import json
import os

DATA_DIR = "dataset/generated"
VALID_TYPES = {"direct_injection", "roleplay", "reformulation", "multiturn"}
VALID_DIFFICULTIES = {"easy", "medium", "hard"}


def validate_file(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ids = set()

    for item in data:
        assert "id" in item, f"Missing id in {path}"
        assert item["id"] not in ids, f"Duplicate id {item['id']} in {path}"
        ids.add(item["id"])

        assert item.get("type") in VALID_TYPES, f"Invalid type in {path}: {item.get('type')}"
        assert item.get("difficulty") in VALID_DIFFICULTIES, f"Invalid difficulty in {path}: {item.get('difficulty')}"
        assert item.get("language") == "fr", f"Invalid language in {path}"
        assert item.get("expected_behavior") == "refuse_or_resist", f"Invalid expected_behavior in {path}"
        assert "subtype" in item and item["subtype"], f"Missing subtype in {path}"

        if item["type"] == "multiturn":
            assert "turns" in item, f"Missing turns in multiturn item {item['id']}"
            assert isinstance(item["turns"], list), f"turns must be list in item {item['id']}"
            assert len(item["turns"]) >= 2, f"Not enough turns in item {item['id']}"
            for turn in item["turns"]:
                assert isinstance(turn, str) and turn.strip(), f"Empty turn in item {item['id']}"
        else:
            assert "prompt" in item, f"Missing prompt in item {item['id']}"
            assert isinstance(item["prompt"], str) and item["prompt"].strip(), f"Empty prompt in item {item['id']}"

    print(f"OK: {path} ({len(data)} items)")


def main():
    for filename in sorted(os.listdir(DATA_DIR)):
        if filename.endswith(".json"):
            validate_file(os.path.join(DATA_DIR, filename))
    print("Validation terminée avec succès.")


if __name__ == "__main__":
    main()