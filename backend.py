ruta = r"./great_projects/01_monuments_copy.txt"

class Monument:
    # def __init__(self, name, provence, built_date, build_time, build_cost, moveable, moveing_speed, 
    #             starting_tier, monument_type, build_trigger, on_built, on_destroyed, 
    #             can_use_modifiers_trigger, can_upgrade_trigger, keep_trigger, 
    #             tier_0_upgradeTime, tier_0_costToUpgrade, tier_0_provinceModifiers, 
    #             tier_0_areaModifiers, tier_0_countryModifiers, tier_0_onUpgraded, 
    #             tier_1_upgradeTime, tier_1_costToUpgrade, tier_1_provinceModifiers, 
    #             tier_1_areaModifiers, tier_1_countryModifiers, tier_1_onUpgraded, 
    #             tier_2_upgradeTime, tier_2_costToUpgrade, tier_2_provinceModifiers, 
    #             tier_2_areaModifiers, tier_2_countryModifiers, tier_2_onUpgraded, 
    #             tier_3_upgradeTime, tier_3_costToUpgrade, tier_3_provinceModifiers, 
    #             tier_3_areaModifiers, tier_3_countryModifiers, tier_3_onUpgraded):
    #     '''
    #     Args:
    #         name(string): monument's name
    #         provence(int): province code
    #         built_date(string): yyy.01.01 or yyyy.01.01
    #         build_time(int): time to build
    #         build_cost(int): how much to build one
    #         moveable(string): can we move it? (yes/no)
    #         moveing_speed(int): time to move the project one unit of distance, in days
    #         starting_tier(int): tier that the project starts at when first placed in the game (0/1/2/3)
    #         monument_type(string): project type (monument)
    #         build_trigger: can we build it?
    #         on_built: what to do when it's built
    #         on_destroyed: what to do when it's destroyed
    #         can_use_modifiers_trigger: can our country use it?
    #         can_upgrade_trigger: can our country upgrade it?
    #         keep_trigger: can our country keep it or is it destroyed when we get hold of it?

    #         tier_x_upgradeTime(int): Description
    #         tier_x_costToUpgrade(int): Description
    #         tier_x_yyyyModifiers(list): Description
    #         tier_x_onUpgraded(list): Description
    #     '''
    #     self.name = name
    #     self.start = provence
    #     self.date = built_date
    #     self.time = build_time  #block
    #     self.build_cost = build_cost
    #     self.can_be_moved = moveable
    #     self.move_days_per_unit_distance = moveing_speed
    #     self.starting_tier = starting_tier
    #     self.type = monument_type
    #     self.build_trigger = build_trigger  #block
    #     self.on_built = on_built  #block
    #     self.on_destroyed = on_destroyed  #block
    #     self.can_use_modifiers_trigger = can_use_modifiers_trigger  #block
    #     self.can_upgrade_trigger = can_upgrade_trigger  #block
    #     self.keep_trigger = keep_trigger  #block

    #     self.tier_0_upgrade_time = tier_0_upgradeTime
    #     self.tier_0_cost_to_upgrade = tier_0_costToUpgrade
    #     self.tier_0_province_modifiers = tier_0_provinceModifiers
    #     self.tier_0_area_modifier = tier_0_areaModifiers
    #     self.tier_0_country_modifiers = tier_0_countryModifiers
    #     self.tier_0_on_upgraded = tier_0_onUpgraded

    #     self.tier_1_upgrade_time = tier_1_upgradeTime
    #     self.tier_1_cost_to_upgrade = tier_1_costToUpgrade
    #     self.tier_1_province_modifiers = tier_1_provinceModifiers
    #     self.tier_1_area_modifier = tier_1_areaModifiers
    #     self.tier_1_country_modifiers = tier_1_countryModifiers
    #     self.tier_1_on_upgraded = tier_1_onUpgraded

    #     self.tier_2_upgrade_time = tier_2_upgradeTime
    #     self.tier_2_cost_to_upgrade = tier_2_costToUpgrade
    #     self.tier_2_province_modifiers = tier_2_provinceModifiers
    #     self.tier_2_area_modifier = tier_2_areaModifiers
    #     self.tier_2_country_modifiers = tier_2_countryModifiers
    #     self.tier_2_on_upgraded = tier_2_onUpgraded

    #     self.tier_3_upgrade_time = tier_3_upgradeTime
    #     self.tier_3_cost_to_upgrade = tier_3_costToUpgrade
    #     self.tier_3_province_modifiers = tier_3_provinceModifiers
    #     self.tier_3_area_modifier = tier_3_areaModifiers
    #     self.tier_3_country_modifiers = tier_3_countryModifiers
    #     self.tier_3_on_upgraded = tier_3_onUpgraded


    def __init__(self, name:str, data_dict:dict):
        '''
        Docstring for __init__
        Args:
            no_limit_tag(bool): remove or not its build, upgrade and use restriction
            name(string): monument's name
            provence(int): province code
            built_date(string): yyy.01.01 or yyyy.01.01
            build_time(int): time to build
            build_cost(int): how much to build one
            moveable(string): can we move it? (yes/no)
            moveing_speed(int): time to move the project one unit of distance, in days
            starting_tier(int): tier that the project starts at when first placed in the game (0/1/2/3)
            monument_type(string): project type (monument)
            build_trigger: can we build it?
            on_built: what to do when it's built
            on_destroyed: what to do when it's destroyed
            can_use_modifiers_trigger: can our country use it?
            can_upgrade_trigger: can our country upgrade it?
            keep_trigger: can our country keep it or is it destroyed when we get hold of it?

            tier_x_upgradeTime(int): Description
            tier_x_costToUpgrade(int): Description
            tier_x_yyyyModifiers(list): Description
            tier_x_onUpgraded(list): Description
        '''
        self.no_limit_tag = False
        self.name = name
        self.start = data_dict["start"]
        self.date = data_dict["date"]
        self.time = data_dict["time"]["months"]
        self.build_cost = data_dict["build_cost"]
        self.can_be_moved = data_dict["can_be_moved"]
        self.move_days_per_unit_distance = data_dict["move_days_per_unit_distance"]
        self.starting_tier = data_dict["starting_tier"]
        self.type = data_dict["type"]
        self.build_trigger = data_dict["build_trigger"]
        self.on_built = data_dict["on_built"]
        self.on_destroyed = data_dict["on_destroyed"]
        self.can_use_modifiers_trigger = data_dict["can_use_modifiers_trigger"]
        self.can_upgrade_trigger = data_dict["can_upgrade_trigger"]
        self.keep_trigger = data_dict["keep_trigger"]

        self.tier_0_upgrade_time = data_dict["tier_0"]["upgrade_time"]
        self.tier_0_cost_to_upgrade = data_dict["tier_0"]["cost_to_upgrade"]
        self.tier_0_province_modifiers = data_dict["tier_0"]["province_modifiers"]
        self.tier_0_area_modifier = data_dict["tier_0"]["area_modifier"]
        self.tier_0_country_modifiers = data_dict["tier_0"]["country_modifiers"]
        self.tier_0_on_upgraded = data_dict["tier_0"]["on_upgraded"]

        self.tier_1_upgrade_time = data_dict["tier_1"]["upgrade_time"]
        self.tier_1_cost_to_upgrade = data_dict["tier_1"]["cost_to_upgrade"]
        self.tier_1_province_modifiers = data_dict["tier_1"]["province_modifiers"]
        self.tier_1_area_modifier = data_dict["tier_1"]["area_modifier"]
        self.tier_1_country_modifiers = data_dict["tier_1"]["country_modifiers"]
        self.tier_1_on_upgraded = data_dict["tier_1"]["on_upgraded"]

        self.tier_2_upgrade_time = data_dict["tier_2"]["upgrade_time"]
        self.tier_2_cost_to_upgrade = data_dict["tier_2"]["cost_to_upgrade"]
        self.tier_2_province_modifiers = data_dict["tier_2"]["province_modifiers"]
        self.tier_2_area_modifier = data_dict["tier_2"]["area_modifier"]
        self.tier_2_country_modifiers = data_dict["tier_2"]["country_modifiers"]
        self.tier_2_on_upgraded = data_dict["tier_2"]["on_upgraded"]

        self.tier_3_upgrade_time = data_dict["tier_3"]["upgrade_time"]
        self.tier_3_cost_to_upgrade = data_dict["tier_3"]["cost_to_upgrade"]
        self.tier_3_province_modifiers = data_dict["tier_3"]["province_modifiers"]
        self.tier_3_area_modifier = data_dict["tier_3"]["area_modifier"]
        self.tier_3_country_modifiers = data_dict["tier_3"]["country_modifiers"]
        self.tier_3_on_upgraded = data_dict["tier_3"]["on_upgraded"]

    
    def time_to_build_block(self, indent=1):
        '''
        Return the 
                    time = {
                        months = build_time
                    }
        block
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        block = (f"{tab_co}time = {{\n"
                 f"{tab}months = {self.time}\n"
                 f"{tab_co}}}\n"
                )
        return block
    

    def build_trigger_block(self, current_dict, current_key="build_trigger", indent=1):
        '''
        Rebuit the
        
                    build_trigger = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            for key, value in current_dict.items():
                if isinstance(value, dict):
                    lines.append(f"{tab}{current_key} = {{")
                    lines.append(self.build_trigger_block(value, key, indent+1))
                    lines.append(f"{tab}}}")
                elif value == None:
                    continue
                else:
                    lines.append(f"{key} = {value}")
            block = "\n".join(lines) + "\n"

        return block
    

    def on_built_block(self, current_dict, current_key="on_built", indent=1):
        '''
        Rebuit the
        
                    on_built = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        lines = []
        for key, value in current_dict.items():
            if isinstance(value, dict):
                lines.append(f"{tab}{current_key} = {{")
                lines.append(self.on_built_block(value, key, indent+1))
                lines.append(f"{tab}}}")
            elif value == None:
                continue            
            else:
                lines.append(f"{key} = {value}")
        block = "\n".join(lines) + "\n"

        return block
    

    def on_destroyed_block(self, current_dict, current_key="on_destroyed", indent=1):
        '''
        Rebuit the
        
                    on_destroyed = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        lines = []
        for key, value in current_dict.items():
            if isinstance(value, dict):
                lines.append(f"{tab}{current_key} = {{")
                lines.append(self.on_destroyed_block(value, key, indent+1))
                lines.append(f"{tab}}}")
            elif value == None:
                continue   
            else:
                lines.append(f"{key} = {value}")
        block = "\n".join(lines) + "\n"

        return block
    

    def can_use_modifiers_trigger_block(self, current_dict, current_key="can_use_modifiers_trigger", indent=1):
        '''
        Rebuit the
        
                    can_use_modifiers_trigger = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            for key, value in current_dict.items():
                if isinstance(value, dict):
                    lines.append(f"{tab}{current_key} = {{")
                    lines.append(self.can_use_modifiers_trigger_block(value, key, indent+1))
                    lines.append(f"{tab}}}")
                elif value == None:
                    continue
                else:
                    lines.append(f"{key} = {value}")
            block = "\n".join(lines) + "\n"

        return block
    

    def can_upgrade_trigger_block(self, current_dict, current_key="can_upgrade_trigger", indent=1):
        '''
        Rebuit the
        
                    can_upgrade_trigger = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            for key, value in current_dict.items():
                if isinstance(value, dict):
                    lines.append(f"{tab}{current_key} = {{")
                    lines.append(self.can_upgrade_trigger_block(value, key, indent+1))
                    lines.append(f"{tab}}}")
                elif value == None:
                    continue
                else:
                    lines.append(f"{key} = {value}")
            block = "\n".join(lines) + "\n"

        return block
    

    def keep_trigger_block(self, current_dict, current_key="keep_trigger", indent=1):
        '''
        Rebuit the
        
                    keep_trigger = {
                        ......
                    }
        block

        Args:
             current_dict(dict): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        '''
        tab = "\t" * indent
        lines = []
        for key, value in current_dict.items():
            if isinstance(value, dict):
                lines.append(f"{tab}{current_key} = {{")
                lines.append(self.keep_trigger_block(value, key, indent+1))
                lines.append(f"{tab}}}")
            elif value == None:
                continue   
            else:
                lines.append(f"{key} = {value}")
        block = "\n".join(lines) + "\n"

        return block
    

    def tier_0_block(self):
        tier0 = Tiers("tier_0", self.tier_0_upgrade_time, self.tier_0_cost_to_upgrade, self.tier_0_province_modifiers, 
                      self.tier_0_area_modifier, self.tier_0_country_modifiers, self.tier_0_on_upgraded)
        return tier0.build_up_tiers()
    

    def tier_1_block(self):
        tier1 = Tiers("tier_1", self.tier_1_upgrade_time, self.tier_1_cost_to_upgrade, self.tier_1_province_modifiers, 
                      self.tier_1_area_modifier, self.tier_1_country_modifiers, self.tier_1_on_upgraded)
        return tier1.build_up_tiers()
    

    def tier_2_block(self):
        tier2 = Tiers("tier_2", self.tier_2_upgrade_time, self.tier_2_cost_to_upgrade, self.tier_2_province_modifiers, 
                      self.tier_2_area_modifier, self.tier_2_country_modifiers, self.tier_2_on_upgraded)
        return tier2.build_up_tiers()
    
    
    def tier_3_block(self):
        tier3 = Tiers("tier_3", self.tier_3_upgrade_time, self.tier_3_cost_to_upgrade, self.tier_3_province_modifiers, 
                      self.tier_3_area_modifier, self.tier_3_country_modifiers, self.tier_3_on_upgraded)
        return tier3.build_up_tiers()
    

    def build_up_the_whole(self, indent=0):
        tab = "\t" * (indent+1)

        lines = []
        
        lines.append(f"{self.name} = {{")
        
        lines.append(f"{tab}start = {self.start}")
        lines.append(f"{tab}date = {self.date}")
        lines.append(self.time_to_build_block())
        lines.append(f"{tab}build_cost = {self.build_cost}")
        lines.append(f"{tab}can_be_moved = {self.can_be_moved}")
        lines.append(f"{tab}move_days_per_unit_distance = {self.move_days_per_unit_distance}")
        lines.append(f"{tab}starting_tier = {self.starting_tier}")
        lines.append(f"{tab}type = {self.type}")

        lines.append(self.build_trigger_block(self.build_trigger))
        lines.append(self.on_built_block(self.on_built))
        lines.append(self.on_destroyed_block(self.on_destroyed))
        lines.append(self.can_use_modifiers_trigger_block(self.can_use_modifiers_trigger))
        lines.append(self.can_upgrade_trigger_block(self.can_upgrade_trigger))
        lines.append(self.keep_trigger_block(self.keep_trigger))
        lines.append(self.tier_0_block())
        lines.append(self.tier_1_block())
        lines.append(self.tier_2_block())
        lines.append(self.tier_3_block())

        lines.append("}")

        block = "\n".join(lines) + "\n"

        return block
    

class Tiers:
    def __init__(self, tier, upgradeTime, costToUpgrade, provinceModifiers, areaModifiers, countryModifiers, onUpgraded):
        '''
        Docstring for __init__
        Args:
             tier(string): tier_0123
             upgradeTime(int): upgrade time in months
             costToUpgrade(int): build cost factor
             provinceModifiers(dict): dictonary of buffs for province
             areaModifiers(dict): dictonary of buffs for area
             countryModifiers(dict): dictonary of buffs for country
             onUpgraded: Description
        '''
        self.tier = tier
        self.upgrade_time = upgradeTime
        self.cost_to_upgrade = costToUpgrade
        self.province_modifiers = provinceModifiers
        self.area_modifier = areaModifiers
        self.country_modifiers = countryModifiers
        self.on_upgrade = onUpgraded
    

    def upgrade_time_block(self, indent=2):
        '''
        Return the 
                    upgrade_time = {
                        months = upgradeTime
                    }
        format
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        block = (f"{tab_co}upgrade_time = {{\n"
                 f"{tab}months = {self.upgrade_time}\n"
                 f"{tab_co}}}\n"
                )
        return block
    

    def cost_to_upgrade_block(self, indent=2):
        '''
        Return the 
                    cost_to_upgrade = {
                        factor = cost_to_upgrade
                    }
        format
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        block = (f"{tab_co}cost_to_upgrade = {{\n"
                 f"{tab}factor = {self.cost_to_upgrade}\n"
                 f"{tab_co}}}\n"
                )
        return block
    

    def province_modifiers_block(self, indent=2):
        '''
        Return the 
                    provinceModifiers = {
                        buff1 = buff1_value
                        ...
                    }
        format
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        lines = []
        lines.append(f"{tab_co}province_modifiers = {{")
        for buff_name, buff_value in self.province_modifiers.items():
            lines.append(f"{tab}{buff_name} = {buff_value}")
        lines.append(f"{tab_co}}}")

        block = "\n".join(lines) + "\n"

        return block
    

    def area_modifier_block(self, indent=2):
        '''
        Return the 
                    areaModifiers = {
                        buff1 = buff1_value
                        ...
                    }
        format
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        lines = []
        lines.append(f"{tab_co}area_modifier = {{")
        for buff_name, buff_value in self.area_modifier.items():
            lines.append(f"{tab}{buff_name} = {buff_value}")
        lines.append(f"{tab_co}}}")

        block = "\n".join(lines) + "\n"

        return block
    

    def country_modifiers_block(self, indent=2):
        '''
        Return the 
                    countryModifiers = {
                        buff1 = buff1_value
                        ...
                    }
        format
        Args:
             indent(int): indentation
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        lines = []
        lines.append(f"{tab_co}country_modifiers = {{")
        for buff_name, buff_value in self.country_modifiers.items():
            lines.append(f"{tab}{buff_name} = {buff_value}")
        lines.append(f"{tab_co}}}")

        block = "\n".join(lines) + "\n"

        return block
    

    def on_upgrade_block(self, indent=2):
        '''
        Return the 
                    on_upgraded = {
                        bonus1 = bonus1_value
                        ...
                    }
        format
        Args:
             indent(int): indentation
        '''
        return self.on_upgrade
    

    def build_up_tiers(self, indent=1):
        tab = "\t" * indent
        lines = []
        lines.append(f"{tab}{self.tier} = {{")
        lines.append(self.upgrade_time_block())
        lines.append(self.cost_to_upgrade_block())
        lines.append(self.province_modifiers_block())
        lines.append(self.area_modifier_block())
        lines.append(self.country_modifiers_block())
        lines.append(self.on_upgrade_block())

        lines.append(f"{tab}}}")

        block = "\n".join(lines) + "\n"

        return block


def parse_paradox(lines):
    '''
    Parsing the paradox tree style data
    Args:
         lines: the lines at the file
    '''
    stack = [{}]

    for raw in lines:
        line = raw.strip()

        if not line:
            continue

        if line.endswith("{"):
            key = line[:-1].split("=")[0].strip()
            new_block = {}
            stack[-1][key] = new_block
            stack.append(new_block)

        elif line == "}":
            stack.pop()

        elif "=" in line:
            key, value = map(str.strip, line.split("=", 1))
            stack[-1][key] = value

    return stack[0]



def read_monuments(path = ruta):
    '''
    function that reads the file of monuments
    Args:
         path(string): path to the files
    '''
    with open(path, "r") as fl:
        datas = parse_paradox(fl)
    
    monument_dict = {}
    monument_index = 0

    for monument_name, monument_data in datas.items():
        monument_dict[monument_index] = Monument(monument_name, monument_data)

    monument_dict[0].name = "ikkk"
    res = monument_dict[0].build_up_the_whole()

    print(res)

read_monuments()