import unittest
import pygame
import sys

try:
    from game_logic import TicTacToe
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)  # Exit if there's an import issue

class TestTicTacToeUI(unittest.TestCase):
    def setUp(self):
        """Initialize Pygame and create a game instance before each test"""
        pygame.init()
        self.game = TicTacToe()
        self.screen = pygame.display.set_mode((600, 600))  # Reinitialize the screen

    def test_screen_initialization(self):
        """Check if the Pygame screen is set up correctly"""
        self.assertIsNotNone(self.screen, "Screen should be initialized")
        self.assertEqual(self.screen.get_size(), (600, 600), "Screen size should be 600x600")

    def test_mouse_click_event(self):
        """Simulate a mouse click and check if it registers correctly"""
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (100, 100), 'button': 1})
        pygame.event.post(event)
        
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.assertEqual(e.pos, (100, 100), "Mouse click position should be recorded correctly")

    def test_quit_event(self):
        """Simulate a quit event and check if it gets processed"""
        event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(event)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.assertEqual(e.type, pygame.QUIT, "Quit event should be recognized")

    def tearDown(self):
        """Quit Pygame after each test"""
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
