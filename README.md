# Gassy Boi
Measures air quality from the inputs of a SGP30 air quality sensor and pushes slack notificationa when air quality exceeds unsafe thresholds.

![](gassyboi.png)

Add the webhook url in `main.py` file.
<sup>sorry
	<sup>this
		<sup>isnt
			<sup>a
				<sup>config</sup>
			</sup>
		</sup>
	</sup>
</sup>

Run `python  server.py` to get the persistent Http server script up.

Run `python main.py` to get the state machine that pushes slack messages up.