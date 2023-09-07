// Minecraft Player Class
class Player {
    constructor(name) {
      this.name = name;
      this.health = 100;
      this.position = {
        x: 0,
        y: 0,
        z: 0
      };
    }
  
    move(x, y, z) {
      this.position.x += x;
      this.position.y += y;
      this.position.z += z;
      console.log(`${this.name} moved to position (${this.position.x}, ${this.position.y}, ${this.position.z})`);
    }
  
    mineBlock() {
      console.log(`${this.name} is mining a block...`);
      // Code to mine a block goes here
    }
  
    attack(player) {
      console.log(`${this.name} is attacking ${player.name}`);
      // Code for attacking another player goes here
    }
  }
  
  // Create Players
  const player1 = new Player("Steve");
  const player2 = new Player("Alex");
  
  // Player Actions
  player1.move(2, 0, 1);
  player2.move(-1, 0, 3);
  
  player1.mineBlock();
  player2.attack(player1);
  