# RocketLand Economy Simulator
###### Originally made on replit (don't use replit it's terrible now) use [these alternatives](https://noreplit.com) 

## Inspired by a great video by Primer [here](https://www.youtube.com/watch?v=PNtKXWNKGN8)

## Rundown

You start in a world with some buyers, and some sellers.

The sellers are selling rockets, and the buyers buy rockets.

Each seller has their own minimum price which they are willing to sell their rocket for. After all, they're looking to make the most money.

Each buyer has their own maximum price which they are willing to pay. These guys want to get the best deal of course.

Each seller selects a customer to have a transaction with. 

If `buyer.maximum` `>=` `seller.minimum`, a trade happens.

If the trade is successful, the buyer decreases their max by 5 (because they lost money) and the seller increases their min by 5 (to get more MONEY).

If it isn't successful, the buyer increases their max by 5 (to be able to buy more) and the seller decreases their min by 5 (to get more CUSTOMERS).

This happens for each buyer and seller every day.

**Behold! The Economy Simulation of Rocket-land** 🥳🥳🥳🎉🎉🚀🚀🔥🔥

## HOW TO USE

If you wanna tweak the parameters, feel free to do so.

Increasing the number of sellers encourages seller competition.
Increasing the number of buyers encourages buyer competition.