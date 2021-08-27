from cn.nukkit.plugin import PluginBase
from cn.nukkit import Player
from cn.nukkit import Server
join = "%player% join"
quit = "%player% quit"
can_fly_hub = False

class PyEssentials(PluginBase):

	def onEnable(self):
		self.getServer().getLogger().info("PyEssentials enable")

	def onCommand(self, sender, command, label, args):
		cmd = command.getName().lower()
		if cmd == "hub":
			pos = self.getServer().getDefaultLevel().getSafeSpawn()
			sender.teleport(pos)
			sender.sendActionBar("Back to hub")
		if cmd ==  "feed":
			sender.getFoodData().setLevel(20)
		if cmd == "heal":
			sender.setHealth(20)

		if cmd == "fly":
			if sender.getAllowFlight():
				sender.setAllowFlight(False)
				sender.sendActionBar("Disable fly")
			else:
				if sender.getLevel().getName() == self.getServer().getDefaultLevel().getName():	
					if can_fly_hub:
						sender.sendActionBar("Can't fly in hub")
						return True
					sender.sendActionBar("Enable fly")
					sender.setAllowFlight(True)
		if cmd == "clearinv":
			if len(args) == 1:
				player = self.getServer().getPlayer(args[0])
				if player is not None:
					player.getInventory().clearAll()
					player.sendMessage("Inventory cleared by " + sender.getName())
					sender.sendMessage("Clear inventory " + player.getName())
				else:
					sender.sendMessage("Player " + args[0] + " not found")
			else:
				sender.getInventory().clearAll()
		if cmd == "kickall":
			for player in self.getServer().getOnlinePlayers().values():
				player.kick("Kicked from the server", False)
		if cmd == "tpall":
			for player in self.getServer().getOnlinePlayers().values():
				player.sendMessage("Teleport to " + sender.getName())
				player.teleport(sender)
		if cmd == "clearchat":
			for i in range(1, 100):
				sender.sendMessage("")
			sender.sendMessage("You Cleared Your Chat")
		if cmd == "clearglobalchat":
			for i in range(1, 100):
				self.getServer().broadcastMessage("")
			self.getServer().broadcastMessage("Global Chat Cleared")

def PlayerJoinEvent(e):
	e.setJoinMessage(join.replace("%player%", e.getPlayer().getName()))

def PlayerQuitEvent(e):
	e.setJoinMessage(join.replace("%player%", e.getPlayer().getName()))