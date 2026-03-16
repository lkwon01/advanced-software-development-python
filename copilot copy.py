
from datetime import datetime, date
import sys


def get_birthday(prompt="Enter your birthday (YYYY-MM-DD): ", attempts=3):
	"""Prompt the user up to `attempts` times and return a date.

	Raises ValueError if no valid date is entered.
	"""
	for attempt in range(1, attempts + 1):
		s = input(prompt).strip()
		if not s:
			print("Empty input — please enter a date or type 'q' to quit.")
			continue
		if s.lower() in ("q", "quit", "exit"):
			raise SystemExit("User cancelled input")
		# quick validation for common invalid February dates
		parts = s.split("-")
		if len(parts) == 3 and all(p.isdigit() for p in parts):
			y, m, d = map(int, parts)
			if m == 2 and d in (30, 31):
				raise ValueError(f"Invalid date: February {d} does not exist")
			if m == 2 and d == 29:
				# check leap year
				is_leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
				if not is_leap:
					raise ValueError(f"Invalid date: February 29, {y} is not in a leap year")
		try:
			return datetime.strptime(s, "%Y-%m-%d").date()
		except ValueError:
			print("Invalid date. Use format YYYY-MM-DD (e.g. 1990-12-31).")
			if attempt < attempts:
				print(f"Attempts remaining: {attempts - attempt}")
	raise ValueError("Failed to provide a valid date")


def main():
	try:
		birthday = get_birthday()
		today = date.today()
		days_difference = abs((today - birthday).days)
	except SystemExit as e:
		print(e)
		return 1
	except ValueError as e:
		print("Error:", e)
		return 2
	except Exception as e:
		print("Unexpected error:", e)
		return 3

print("Number of days between today and your birthday:", days_difference)

if __name__ == "__main__":
	sys.exit(main())