
from io import StringIO
from unittest.mock import patch

from util import parse_file
from robot import Robot


class TestToyRobot:
    def test_valid_commands(self):
        # setup
        robot_obj = Robot()

        # execute
        # verify
        with patch('sys.stdout', new=StringIO()) as patched_stdout:
            parse_file(
                [
                    "PLACE 1,2,EAST",     # 1,2 E
                    "MOVE",               # 2,2 E
                    "MOVE",               # 3,2 E  
                    "LEFT",               # 3,2 N
                    "MOVE",               # 3,3 N
                    "MOVE",               # 3,4 N 
                    "RIGHT",              # 3,4 E
                    "MOVE",               # 4,4 E
                    "MOVE",               # COMMAND SHOULD BE IGNORED as robot would fall
                    "REPORT"
                ],
                robot_obj
            )
            assert 'X: 4, Y:4, F:EAST' in patched_stdout.getvalue().strip()
            # test report outputs coordinates correctly 
        assert robot_obj.x == 4 and robot_obj.y == 4 and robot_obj.position == 'EAST' 
    
    def test_incorrect_commands(self):
        robot_obj = Robot()

        # execute
        # verify
        parse_file(
            [
                "PLACE -1,2,EAST",    # INVALID
                "LEFT",               # NOT PLACED
                "MOVE",               # NOT PLACED
                "UNREGISTERD_CMD",    # Illegal command
                "REPORT"
            ],
            robot_obj
        ) 
        assert robot_obj.x == None and robot_obj.y == None and robot_obj.position == None
    
    def test_fuzzy_order(self): 
        robot_obj = Robot()
        parse_file(
            [
                "REPORT",             # NOT PLACED
                "LEFT",               # NOT PLACED
                "MOVE",               # NOT PLACED
                "RIGHT",              # NOT PLACED
                "PLACE 4,4,NORTH",    # CORNER PLACEMENT
                "MOVE",               # IGNORED - Would fall off 
                "LEFT",               # VALID - 4,4 WEST
                "MOVE",                # VALID - 3,4 WEST
                "LEFT",               # VALID - 3,4 SOUTH
                "MOVE",               # VALID - 3,3 SOUTH
                "REPORT"
            ],
            robot_obj
        )
        assert robot_obj.x == 3 and robot_obj.y == 3 and robot_obj.position == 'SOUTH'

    def test_multiple_place_cmds(self): 
        robot_obj = Robot()
        parse_file(
            [
                "PLACE 3,4,NORTH",              # PLACE
                "PLACE HERE<THERE,EVERYWHERE",  #INVALID PLACE
                "PLACE 4,4,NORTH",              # CORNER PLACEMENT
                "REPORT"
            ],
            robot_obj
        )
        assert robot_obj.x == 4 and robot_obj.y == 4 and robot_obj.position == 'NORTH'

    def test_multiple_reports(self): 
        robot_obj = Robot()
        with patch('sys.stdout', new=StringIO()) as patched_stdout:
            parse_file(
                [
                    "PLACE 1,2,EAST",     # 1,2 E
                    "REPORT",             # 1,2 E
                    "MOVE",               # 2,2 E  
                    "REPORT",             # 2,2 E
                ],
                robot_obj
            )
            assert 'X: 1, Y:2, F:EAST' in patched_stdout.getvalue().strip()
            assert 'X: 2, Y:2, F:EAST' in patched_stdout.getvalue().strip()
