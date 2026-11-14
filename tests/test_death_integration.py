import time
from datetime import timedelta

from package import interaction
from package.pet import create_pet


def test_alive_pet():
    pet = create_pet("Buddy")
    now = 2000000000
    pet["last_seen"] = now - 60

    assert interaction.check_saved_death(pet, now) is False
    assert pet["alive"] is True
    assert pet["health"] == 100


def test_death_after_seven_days():
    pet = create_pet("Buddy")
    now = 2000000000
    pet["last_seen"] = now - 7 * 24 * 60 * 60

    assert interaction.check_saved_death(pet, now) is True
    assert pet["alive"] is False
    assert pet["health"] == 100


def test_alive_before_seven_days():
    pet = create_pet("Buddy")
    now = 2000000000
    pet["last_seen"] = now - 6 * 24 * 60 * 60

    assert interaction.check_saved_death(pet, now) is False
    assert pet["alive"] is True


def test_death_from_low_health():
    pet = create_pet("Buddy")
    now = 2000000000
    pet["last_seen"] = now
    pet["health"] = 10

    assert interaction.check_saved_death(pet, now) is True
    assert pet["alive"] is False


def test_missing_timestamp():
    pet = create_pet("Buddy")

    assert interaction.check_saved_death(pet) is False
    assert pet["alive"] is True


def test_replace_dead_pet(monkeypatch, tmp_path):
    old_pet = create_pet("Buddy")
    old_pet["alive"] = False

    new_pet = create_pet("Mochi")

    save_file = tmp_path / "pet.json"

    monkeypatch.setattr(interaction, "SAVE_FILE", save_file)
    monkeypatch.setattr(
        interaction, "draw_screen",
        lambda *args: None
    )
    monkeypatch.setattr(
        interaction, "create_pet",
        lambda: new_pet
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda message="": ""
    )

    result = interaction.replace_dead_pet(old_pet)
    loaded = interaction.load_pet(save_file)

    assert result["name"] == "Mochi"
    assert loaded["name"] == "Mochi"
    assert loaded["alive"] is True
    assert old_pet["alive"] is False
