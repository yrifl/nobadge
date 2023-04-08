# Skids are cringes.
# Author: @yrifl (xYuri#7125)

from time import sleep
from os import system
import requests, json

class NoBadge:
	def __self__(self, uid, cookie):
		print('Fetching badges...')

		self.badges = requests.get(f'https://badges.roblox.com/v1/users/{uid}/badges?limit=100&sortOrder=Asc')
		self.result = json.loads(
			self.badges.text
		)

		# ...
		print('Setting up the environment..')

		self.Id = []
		self.BadgeName = []
		self.PlaceID = []
		self.GameName = []

		self.Cookies = {
			'.ROBLOSECURITY': cookie
		}

		print('Creating headers..')
		self.xcsrftoken = requests.post(
			"https://auth.roblox.com/v2/logout", cookies=self.Cookies
		).headers['X-CSRF-TOKEN']

		self.Headers = {
			'Content-Type': 'application/json',
			'X-CSRF-TOKEN': self.xcsrftoken
		}

		self.Success = 0

	def Exec(self):
		for Id in range(len(self.result["data"])):
			self.Id.append(
				self.result["data"][Id]["id"]
			)

			self.BadgeName(
				self.result["data"][Id]["name"]
			)

		for PlaceID in range(len(self.result["data"])):
			self.PlaceID.append(
				self.result["data"][PlaceID]["awarder"]["id"]
			)

		for GameName in range(len(self.PlaceID)):
			_ = requests.get(f'https://games.roblox.com/v1/games/multiget-place-details?placeIds={self.PlaceID[GameName]}', cookies = self.Cookies)
			_ = json.loads(
				_.text
			)

		for _ in range(len(self.Id)):
			print(f'Trying to delete badge named {self.BadgeName[_]} from {self.GameName[_]} game with badge id {self.Id[_]}')
			r = requests.delete(
				f"https://badges.roblox.com/v1/user/badges/{self.Id[_]}",
				cookies = self.Cookies,
				headers = self.Headers
			)

			if r.status_code == 200:
				self.Success += 1

		if len(self.Id) != self.Success:
			if self.Success == 0:
				print('Cannot remove any badges.. check your userid, or cookies.')
				print('Made issue on github, if no works.')
			else:
				print(f"Successfully removed {self.Success} badges, failed to remove {len(self.Id)-self.Success} badges.")
				print("Try to re-run the program.")

		else:
			print(f"All badges removed, badges removed: {self.Success}")

		print("Thanks for using me! Author: xYuri#7125")

if __name__ == "__main__":
	uid = int(
		input("(User ID) > ")
	)

	rbxcookie = str(
		input("(.ROBLOSECURITY) > ")
	)

	NoBadge = NoBadge(uid, rbxcookie)
	NoBadge.Exec()