# Скрипт осуществляет произведение автоматических скриншотов по расписанию на ptz
# по предустановленным пресетам или в режиме патрулирования в красной зоне расписания

# <parameter>
#         <id>SELECTED_SERVER</id>
#         <type>server</type>
#         <name>Server</name>
#     </parameter>
#     <parameter>
#         <id>SELECTED_CHANNELS</id>
#         <type>objects</type>
#         <name>Channels</name>
#     </parameter>
# SELECTED_CHANNELS = GLOBALS.get("SELECTED_CHANNELS", '')
# this params will use for many channels at a server
"""
<parameters>
    <company>AATrubilinAndDMMiskevich</company>
    <title>PTZScreenshotsAutomation</title>
    <version>1.0</version>

    <parameter>
        <id>CHANNEL</id>
        <type>channel</type>
        <name>Channel</name>
        <value></value>
    </parameter>
    <parameter>
        <id>SCHEDULE</id>
        <type>objects</type>
        <name>Work by schedule</name>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Workmode</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_GREED</id>
        <name>Default mode (Green or without schedule)</name>
        <value>Patrol</value>
        <string_list>Patrol,Preset</string_list>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_RED</id>
        <name>Alarm mode (Red)</name>
        <value>Off</value>
        <string_list>Patrol,Preset,Off</string_list>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_BLUE</id>
        <name>Other mode (Blue)</name>
        <value>Off</value>
        <string_list>Patrol,Preset,Off</string_list>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Patrol settings</name>
    </parameter>
    <parameter>
        <id>DEFAULT_PRESET</id>
        <type>integer</type>
        <name>Default preset</name>
        <value>1</value>
        <min>1</min>
        <max>99</max>
    </parameter>
    <parameter>
        <id>PATROL_PATH</id>
        <type>string</type>
        <name>Patrol path</name>
        <value>1,2,3,4</value>
    </parameter>
    <parameter>
        <id>PATROL_PRESET_TIMEOUT</id>
        <type>integer</type>
        <name>Preset timeout, sec</name>
        <value>30</value>
        <min>15</min>
        <max>9999</max>
    </parameter>
    <parameter>
        <id>PATROL_PRESET_TIMEOUT_RAND_MAX</id>
        <type>integer</type>
        <name>Max random preset timeout, sec</name>
        <value>30</value>
        <min>15</min>
        <max>9999</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Timeout</name>
    </parameter>
    <parameter>
        <id>PTZ_EVENTS_TIMEOUT</id>
        <type>integer</type>
        <name>ActiveDom / User inactivity, sec</name>
        <value>15</value>
        <min>15</min>
        <max>999</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Other</name>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Screenshots</name>
    </parameter>
    <parameter>
        <id>FOLDER_NAME</id>
        <type>string</type>
        <name>folder name</name>
        <value>default</value>
    </parameter>
    <parameter>
        <id>FILE_NAME</id>
        <type>string</type>
        <name>file name</name>
        <value>default</value>
    </parameter>
    <parameter>
        <id>CYCLES_SCREENS</id>
        <type>integer</type>
        <name>number of cycles</name>
        <value>1</value>
    </parameter>
    <parameter>
        <id>PER_HOURS_SCREENS</id>
        <type>integer</type>
        <name>per hours</name>
        <value>1</value>
    </parameter>

    <resources>
        <resource>shot_saver.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

resources = {
    "shot_saver.py": """
        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
    """,
    "helpers.py": """
        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
    """,
    "schedule.py": """
        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
        kIw=
    """,
}
t1utils.resources_check(script_path, resources)

GLOBALS = globals()

CHANNEL = GLOBALS.get("CHANNEL", None)
SCHEDULE = GLOBALS.get("SCHEDULE", "")

WORKMODE_GREED = GLOBALS.get("WORKMODE_GREED", "Patrol")
WORKMODE_RED = GLOBALS.get("WORKMODE_RED", "Off")
WORKMODE_BLUE = GLOBALS.get("WORKMODE_BLUE", "Off")

DEFAULT_PRESET = GLOBALS.get("DEFAULT_PRESET", 1)
PATROL_PATH = GLOBALS.get("PATROL_PATH", "1,2,3,4")
PATROL_PRESET_TIMEOUT = GLOBALS.get("PATROL_PRESET_TIMEOUT", 30)
PATROL_PRESET_TIMEOUT_RAND_MAX = GLOBALS.get("PATROL_PRESET_TIMEOUT_RAND_MAX", 30)

PTZ_EVENTS_TIMEOUT = GLOBALS.get("PTZ_EVENTS_TIMEOUT", 15)

DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "PTZAutomation"

FOLDER_NAME = GLOBALS.get("FOLDER_NAME", "default")
FILE_NAME = GLOBALS.get("FILE_NAME", "default")

CYCLES_SCREENS = GLOBALS.get("CYCLES_SCREENS", 1)
PER_HOURS_SCREENS = GLOBALS.get("PER_HOURS_SCREENS", 1)
per_time = PER_HOURS_SCREENS * 3600


from shot_saver import ShotSaver
import time
import random
from itertools import cycle
from __builtin__ import object

import os
import datetime
import host

import helpers

helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

from schedule import ScheduleObject

assert CHANNEL, "Channel not selected"
channel = host.object(CHANNEL.split("_")[0])
try:
    channel.state("signal")
except EnvironmentError:
    raise EnvironmentError("Channel %s not found or disabled" % CHANNEL)


def __get_random_timout():
    return random.randint(PATROL_PRESET_TIMEOUT, PATROL_PRESET_TIMEOUT_RAND_MAX)


if PATROL_PRESET_TIMEOUT == PATROL_PRESET_TIMEOUT_RAND_MAX:

    def get_timeout():
        return PATROL_PRESET_TIMEOUT


else:
    assert (
            PATROL_PRESET_TIMEOUT < PATROL_PRESET_TIMEOUT_RAND_MAX
    ), "Random max timeout must be lower then preset timeout"


    def get_timeout():
        return __get_random_timout()


class PTZAutomation(object):
    default_shots_folder = host.settings("system_wide_options")[
        "screenshots_folder"]

    def __init__(self, channel):
        self.channel = channel
        self.get_timeout = lambda: 30
        self.default_preset = 1
        self.ad_timeout = 15
        self.patrol_path = [1, 2, 3, 4]
        self._already_in_preset = False
        self.ss = ShotSaver()
        self.color_now = 'Green'

        self.len_path = 0
        self.__cycles_passed = 0
        self.last_time_change = 0

        self.__current_index_preset = 0

        self.__workmode = {
            "Green": self.patrol,
            "Red": self.do_nothing,
            "Blue": self.do_nothing,
        }

        self.__last_ad_activity_ts = 0
        self.__current_work_mode = "patrol"

    @property
    def patrol_path(self):
        current = self.current_preset
        self.current_index_preset += 1
        return current

    @property
    def already_in_preset(self):
        return self._already_in_preset

    @property
    def current_preset(self):
        return self.__patrol_path[self.current_index_preset]

    @property
    def cycles_passed(self):
        return self.__cycles_passed

    @property
    def current_index_preset(self):
        return self.__current_index_preset

    @already_in_preset.setter
    def already_in_preset(self, value):
        self._already_in_preset = value

    @patrol_path.setter
    def patrol_path(self, value):
        if isinstance(value, str):
            assert value, "Patrol path is empty"
            value = [int(v) for v in value.split(",")]
        self.len_path = len(value)
        self.__patrol_path = value
        # self.__patrol_path = cycle(value)
        logger.debug("Set new patrol path: cycle(%r)", value)

    @cycles_passed.setter
    def cycles_passed(self, value):
        self.__cycles_passed = value

    @current_index_preset.setter
    def current_index_preset(self, value):
        if value > self.len_path - 1:
            self.__current_index_preset = 0
            self.cycles_passed += 1
        else:
            self.__current_index_preset = value

    def set_mode(self, color, mode):
        mode = mode.lower()
        if mode == "patrol":
            self.__workmode[color] = self.patrol
        elif mode == "preset":
            self.__workmode[color] = self.preset
        else:
            self.__workmode[color] = self.do_nothing
        logger.debug("Change mode: %s", self.__workmode)

    def set_preset(self, preset):
        file_path = os.path.join(self.default_shots_folder, FOLDER_NAME)
        dt = datetime.datetime.now()
        str_dt = dt.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = FILE_NAME + str_dt + "(" + str(preset) + ").jpg"
        logger.debug("%s go to %s", channel.name, preset)
        self.channel.ptz_preset(preset)
        if self.color_now == 'Red':
            if self.cycles_passed >= CYCLES_SCREENS and time.time() - self.last_time_change > per_time:
                self.cycles_passed = 0
            if self.cycles_passed < CYCLES_SCREENS:
                self.last_time_change = time.time()
                host.timeout(10000, lambda: self.ss.save(CHANNEL, dt=None, file_path=file_path, file_name=file_name))

    def patrol(self):
        if self.__current_work_mode == "patrol":
            if time.time() - self.__last_ad_activity_ts > self.ad_timeout:
                self.set_preset(self.patrol_path)
                timeout = self.get_timeout()
                logger.debug("Go next preset after %s", timeout)
                host.timeout(timeout * 1000, self.patrol)
            else:
                host.timeout(1000, self.patrol)

    def preset(self):
        if self.__current_work_mode == "preset":
            if time.time() - self.__last_ad_activity_ts > self.ad_timeout:
                if not self.already_in_preset:
                    if self.color_now == 'Red':
                        self.cycles_passed += 1
                    self.set_preset(self.default_preset)
                    self.already_in_preset = True
                    host.timeout(1000 * 15, self.preset)
                else:
                    host.timeout(1000 * 15, self.preset)

    def do_nothing(self):
        pass

    def color_change_handler(self, sched):
        assert sched.color in self.__workmode, "Activate the schedule"
        self.current_index_preset = 0
        self.cycles_passed = 0
        self.color_now = sched.color
        work = self.__workmode[sched.color]
        self.__current_work_mode = work.__name__
        logger.info("Start %s mode %s", sched.color, self.__current_work_mode)
        work()

    def run_default(self):
        work = self.__workmode["Green"]
        self.__current_work_mode = work.__name__
        logger.info("Start default mode %s", self.__current_work_mode)
        work()

    def ptz_handler(self, ev):
        logger.debug("ptz_handler: ev %s", ev.type)
        if ev.channel == self.channel.guid:
            if (
                    "PRESET" not in ev.type
                    and "ACQUIRE" not in ev.type
                    and "RELEASE" not in ev.type
            ):
                self.__last_ad_activity_ts = time.time()
                self.already_in_preset = False


ptz = PTZAutomation(channel)
ptz.get_timeout = get_timeout
ptz.default_preset = DEFAULT_PRESET
ptz.patrol_path = PATROL_PATH
ptz.ad_timeout = PTZ_EVENTS_TIMEOUT

ptz.set_mode("Green", WORKMODE_GREED)
ptz.set_mode("Red", WORKMODE_RED)
ptz.set_mode("Blue", WORKMODE_BLUE)

if SCHEDULE:
    schedule = ScheduleObject(
        SCHEDULE,
        color_change_handler=ptz.color_change_handler,
        on_ready_handler=ptz.color_change_handler,
    )
else:
    schedule = None
    ptz.run_default()

host.activate_on_ptz_events(ptz.ptz_handler)
