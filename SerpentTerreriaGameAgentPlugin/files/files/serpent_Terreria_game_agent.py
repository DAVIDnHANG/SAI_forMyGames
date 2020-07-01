from serpent.game_agent import GameAgent


class SerpentTerreriaGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        print('agent read latest frame?')

        for i, game_frame in enumerate(self.game_frame_buffer):
            self.visual_debugger.store_image_data(game_frame.frame, game_frame.frame.shape, str(i))
