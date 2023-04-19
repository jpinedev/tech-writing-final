import mspj_engine

engine = mspj_engine.Engine();

# Initialize the Engine Subsystems
engine.InitializeGraphicsSubSystem();
engine.InitializeInputSystem();
# Once all subsystems have been initialized
# Start the engine
engine.Start();

# ------- all scene setup should happen after this line -------

# Load the texture atlas for the tilemap (where each tile is 32x32 pixels)
engine.LoadTextureAtlas("./images/character-sprite/path/path-sheet.bmp", 32, 32);

# Setup our TileMap
tileMapObject = engine.InstantiateGameObject();
tileMapComponent = engine.InstantiateTileMapComponent(tileMapObject);
# Each 32x32 tile is scaled up to 64x64 pixels.
tileMapComponent.SetDisplayTileSize(64, 64);
# This example tile map is 20x11 in our game.
tileMapComponent.GenerateMapFromFile("./tilemap-levels/level1");

# Note: Player must be created after the tilemap to be rendered after (above) the tilemap
# Create our player game object, all components created here
# are to be deleted by the Player
player = engine.InstantiateGameObject();
# Prepare the controller
controller = engine.InstantiateControllerComponent(player);
player.GetTransform().SetPosition(128, 64);
# Prepare the sprite
sprite = engine.InstantiateSpriteRendererComponent(player);
# Load the spritesheet
playerSpritesheet = mspj_engine.LoadSpritesheet("./images/character-sprite/walk-cycle/character-walk-spritesheet.bmp");
# Set the size of the sprites on the spritesheet (32x32 pixels)
playerSpritesheet.SetSpriteSize(32, 32);
# Assign the spritesheet to the player's sprite renderer
sprite.SetSpritesheet(playerSpritesheet);
# Set the size of the sprite in the world (32x32 pixels)
sprite.SetDisplaySize(32, 32);

# ------- all scene setup should finish before this line -------

# Run our program forever
engine.MainGameLoop();

# Explicitly call Shutdown to terminate our engine
engine.Shutdown();