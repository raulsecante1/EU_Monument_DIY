ruta = r"./great_projects/01_monuments.txt"

class Monument:
    def __init__(self, name, data_list):
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
        self.start = self.get_node(data_list, "start")
        self.date = self.get_node(data_list, "date")
        self.time = self.get_node(self.get_node(data_list, "time"), "months")
        self.build_cost = self.get_node(data_list, "build_cost")
        self.can_be_moved = self.get_node(data_list, "can_be_moved")
        self.move_days_per_unit_distance = self.get_node(data_list, "move_days_per_unit_distance")
        self.starting_tier = self.get_node(data_list, "starting_tier")
        self.type = self.get_node(data_list, "type")
        self.build_trigger = self.get_node(data_list, "build_trigger")

        #some of the monuments dont have the following blocks, and so if for region_modifier and country_modifiers, stupid donkey
        self.on_built = self.ensure_block(data_list, "on_built")
        self.on_destroyed = self.ensure_block(data_list, "on_destroyed")
        
        self.can_use_modifiers_trigger = self.get_node(data_list, "can_use_modifiers_trigger")
        self.can_upgrade_trigger = self.get_node(data_list, "can_upgrade_trigger")
        self.keep_trigger = self.get_node(data_list, "keep_trigger")

        self.tier_0_upgrade_time = self.get_node(self.get_node(self.get_node(data_list, "tier_0"), "upgrade_time"), "months")
        self.tier_0_cost_to_upgrade = self.get_node(self.get_node(self.get_node(data_list, "tier_0"), "cost_to_upgrade"), "factor")
        self.tier_0_province_modifiers = self.get_node(self.get_node(data_list, "tier_0"), "province_modifiers")
        self.tier_0_area_modifier = self.get_node(self.get_node(data_list, "tier_0"), "area_modifier")
        self.tier_0_region_modifier = self.ensure_block(self.get_node(data_list, "tier_0"), "region_modifier")
        self.tier_0_country_modifiers = self.ensure_block(self.get_node(data_list, "tier_0"), "country_modifiers")
        self.tier_0_on_upgraded = self.ensure_block(self.get_node(data_list, "tier_0"), "on_upgraded")

        self.tier_1_upgrade_time = self.get_node(self.get_node(self.get_node(data_list, "tier_1"), "upgrade_time"), "months")
        self.tier_1_cost_to_upgrade = self.get_node(self.get_node(self.get_node(data_list, "tier_1"), "cost_to_upgrade"), "factor")
        self.tier_1_province_modifiers = self.get_node(self.get_node(data_list, "tier_1"), "province_modifiers")
        self.tier_1_area_modifier = self.get_node(self.get_node(data_list, "tier_1"), "area_modifier")
        self.tier_1_region_modifier = self.ensure_block(self.get_node(data_list, "tier_1"), "region_modifier")
        self.tier_1_country_modifiers = self.ensure_block(self.get_node(data_list, "tier_1"), "country_modifiers")
        self.tier_1_on_upgraded = self.ensure_block(self.get_node(data_list, "tier_1"), "on_upgraded")

        self.tier_2_upgrade_time = self.get_node(self.get_node(self.get_node(data_list, "tier_2"), "upgrade_time"), "months")
        self.tier_2_cost_to_upgrade = self.get_node(self.get_node(self.get_node(data_list, "tier_2"), "cost_to_upgrade"), "factor")
        self.tier_2_province_modifiers = self.get_node(self.get_node(data_list, "tier_2"), "province_modifiers")
        self.tier_2_area_modifier = self.get_node(self.get_node(data_list, "tier_2"), "area_modifier")
        self.tier_2_region_modifier = self.ensure_block(self.get_node(data_list, "tier_2"), "region_modifier")
        self.tier_2_country_modifiers = self.ensure_block(self.get_node(data_list, "tier_2"), "country_modifiers")
        self.tier_2_on_upgraded = self.ensure_block(self.get_node(data_list, "tier_2"), "on_upgraded")

        self.tier_3_upgrade_time = self.get_node(self.get_node(self.get_node(data_list, "tier_3"), "upgrade_time"), "months")
        self.tier_3_cost_to_upgrade = self.get_node(self.get_node(self.get_node(data_list, "tier_3"), "cost_to_upgrade"), "factor")
        self.tier_3_province_modifiers = self.get_node(self.get_node(data_list, "tier_3"), "province_modifiers")
        self.tier_3_area_modifier = self.get_node(self.get_node(data_list, "tier_3"), "area_modifier")
        self.tier_3_region_modifier = self.ensure_block(self.get_node(data_list, "tier_3"), "region_modifier")
        self.tier_3_country_modifiers = self.ensure_block(self.get_node(data_list, "tier_3"), "country_modifiers")
        self.tier_3_on_upgraded = self.ensure_block(self.get_node(data_list, "tier_3"), "on_upgraded")

    
    def time_to_build_block(self, indent=1):
        '''
        Return the 
                    time = {
                        months = build_time
                    }
        block
        Args:
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * (indent+1)
        tab_co = "\t" * indent
        block = (f"{tab_co}time = {{\n"
                 f"{tab}months = {self.time}\n"
                 f"{tab_co}}}\n"
                )
        return block
    

    def build_trigger_block(self, current_node, current_key="build_trigger", indent=1):
        '''
        Rebuit the
        
                    build_trigger = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)  # i should have used tab and tab_co, also the list/dict problem, build up a high-level structure 
                                       # and work-flow next time before coding!!!!
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            lines.append(f"{tab}{current_key} = {{")
            for key, value in current_node:
                if isinstance(value, list):
                    lines.append(self.build_trigger_block(value, key, indent+1))
                elif value == None:
                    continue
                else:
                    lines.append(f"{tab_pairs}{key} = {value}")
            lines.append(f"{tab}}}")
            block = "\n".join(lines) + "\n"

        return block
    

    def on_built_block(self, current_node, current_key="on_built", indent=1):
        '''
        Rebuit the
        
                    on_built = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        lines = []
        lines.append(f"{tab}{current_key} = {{")
        for key, value in current_node:
            if isinstance(value, list):
                lines.append(self.on_built_block(value, key, indent+1))
            elif value == None:
                continue
            else:
                lines.append(f"{tab_pairs}{key} = {value}")
        lines.append(f"{tab}}}")
        block = "\n".join(lines) + "\n"

        return block
    

    def on_destroyed_block(self, current_node, current_key="on_destroyed", indent=1):
        '''
        Rebuit the
        
                    on_destroyed = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        lines = []
        lines.append(f"{tab}{current_key} = {{")
        for key, value in current_node:
            if isinstance(value, list):
                lines.append(self.on_destroyed_block(value, key, indent+1))
            elif value == None:
                continue
            else:
                lines.append(f"{tab_pairs}{key} = {value}")
        lines.append(f"{tab}}}")
        block = "\n".join(lines) + "\n"

        return block
    

    def can_use_modifiers_trigger_block(self, current_node, current_key="can_use_modifiers_trigger", indent=1):
        '''
        Rebuit the
        
                    can_use_modifiers_trigger = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            lines.append(f"{tab}{current_key} = {{")
            for key, value in current_node:
                if isinstance(value, list):
                    lines.append(self.can_use_modifiers_trigger_block(value, key, indent+1))
                elif value == None:
                    continue
                else:
                    lines.append(f"{tab_pairs}{key} = {value}")
            lines.append(f"{tab}}}")
            block = "\n".join(lines) + "\n"

        return block
    

    def can_upgrade_trigger_block(self, current_node, current_key="can_upgrade_trigger", indent=1):
        '''
        Rebuit the
        
                    can_upgrade_trigger = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        if self.no_limit_tag:
            block = (f"{tab}{current_key} = {{\n"
                     f"{tab}}}\n"
                    )
        else:
            lines = []
            lines.append(f"{tab}{current_key} = {{")
            for key, value in current_node:
                if isinstance(value, list):
                    lines.append(self.can_upgrade_trigger_block(value, key, indent+1))
                elif value == None:
                    continue
                else:
                    lines.append(f"{tab_pairs}{key} = {value}")
            lines.append(f"{tab}}}")
            block = "\n".join(lines) + "\n"

        return block
    

    def keep_trigger_block(self, current_node, current_key="keep_trigger", indent=1):
        '''
        Rebuit the
        
                    keep_trigger = {
                        ......
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(string)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        lines = []
        lines.append(f"{tab}{current_key} = {{")
        for key, value in current_node:
            if isinstance(value, list):
                lines.append(self.keep_trigger_block(value, key, indent+1))
            elif value == None:
                continue
            else:
                lines.append(f"{tab_pairs}{key} = {value}")
        lines.append(f"{tab}}}")
        block = "\n".join(lines) + "\n"

        return block
    

    def tier_0_block(self):
        tier0 = Tiers("tier_0", self.tier_0_upgrade_time, self.tier_0_cost_to_upgrade, self.tier_0_province_modifiers, 
                      self.tier_0_area_modifier, self.tier_0_region_modifier, self.tier_0_country_modifiers, self.tier_0_on_upgraded)
        return tier0.build_up_tiers()
    

    def tier_1_block(self):
        tier1 = Tiers("tier_1", self.tier_1_upgrade_time, self.tier_1_cost_to_upgrade, self.tier_1_province_modifiers, 
                      self.tier_1_area_modifier, self.tier_1_region_modifier, self.tier_1_country_modifiers, self.tier_1_on_upgraded)
        return tier1.build_up_tiers()
    

    def tier_2_block(self):
        tier2 = Tiers("tier_2", self.tier_2_upgrade_time, self.tier_2_cost_to_upgrade, self.tier_2_province_modifiers, 
                      self.tier_2_area_modifier, self.tier_2_region_modifier, self.tier_2_country_modifiers, self.tier_2_on_upgraded)
        return tier2.build_up_tiers()
    
    
    def tier_3_block(self):
        tier3 = Tiers("tier_3", self.tier_3_upgrade_time, self.tier_3_cost_to_upgrade, self.tier_3_province_modifiers, 
                      self.tier_3_area_modifier, self.tier_3_region_modifier, self.tier_3_country_modifiers, self.tier_3_on_upgraded)
        return tier3.build_up_tiers()
    

    def get_node(self, node, key):
        '''
        function used to access the node like list like dictionary
        Args:
             node(list): the node like list
             key(str): the key of the value to access
        '''
        for k, v in node:
            if k == key:
                return v
        return None
    
    def ensure_block(self, node, key):
        '''
        function to ensure every monument has a block of {key}
        Args:
             node(list): Description
             key(str): the name of the block
        '''
        existing = self.get_node(node, key)
        if existing is None:
            new_block = []
            node.append((key, new_block))
            return new_block
        return existing

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
    def __init__(self, tier, upgradeTime, costToUpgrade, provinceModifiers, areaModifiers, regionModifiers, countryModifiers, onUpgraded):
        '''
        Docstring for __init__
        Args:
             tier(string): tier_0123
             upgradeTime(int): upgrade time in months
             costToUpgrade(int): build cost factor
             provinceModifiers(list): list of buffs for province
             areaModifiers(list): list of buffs for area
             countryModifiers(list): list of buffs for country
             onUpgraded: Description
        '''
        self.tier = tier
        self.upgrade_time = upgradeTime
        self.cost_to_upgrade = costToUpgrade
        self.province_modifiers = provinceModifiers
        self.area_modifier = areaModifiers
        self.region_modifier = regionModifiers
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
        for buff_name, buff_value in self.province_modifiers:
            if buff_name != "" and buff_value != "":
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
        for buff_name, buff_value in self.area_modifier:
            if buff_name != "" and buff_value != "":
                lines.append(f"{tab}{buff_name} = {buff_value}")
        lines.append(f"{tab_co}}}")

        block = "\n".join(lines) + "\n"

        return block
    

    def region_modifier_block(self, indent=2):
        '''
        Return the 
                    regionModifiers = {
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
        lines.append(f"{tab_co}region_modifier = {{")
        for buff_name, buff_value in self.region_modifier:
            if buff_name != "" and buff_value != "":
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
        for buff_name, buff_value in self.country_modifiers:
            if buff_name != "" and buff_value != "":
                lines.append(f"{tab}{buff_name} = {buff_value}")
        lines.append(f"{tab_co}}}")

        block = "\n".join(lines) + "\n"

        return block
    

    def on_upgrade_block(self, current_node, current_key="on_upgrade", indent=2):
        '''
        Return the 
                    on_upgraded = {
                        bonus1 = bonus1_value
                        ...
                    }
        block

        Args:
             current_node(list): the value for the key pair
             current_key(string): the key for the value pair
             indent(int): indentation
        Returns:
             block(str)
        '''
        tab = "\t" * indent
        tab_pairs = "\t" * (indent+1)
        lines = []
        lines.append(f"{tab}{current_key} = {{")
        for key, value in current_node:
            if isinstance(value, list):
                lines.append(self.on_upgrade_block(value, key, indent+1))
            elif value == None:
                continue
            else:
                lines.append(f"{tab_pairs}{key} = {value}")
        lines.append(f"{tab}}}")
        block = "\n".join(lines) + "\n"

        return block
    

    def get_node(self, node, key):
        '''
        function used to access the node like list like dictionary
        Args:
             node(list): the node like list
             key(str): the key of the value to access
        '''
        for k, v in node:
            if k == key:
                return v
        return None
    

    def build_up_tiers(self, indent=1):
        tab = "\t" * indent
        lines = []
        lines.append(f"{tab}{self.tier} = {{")
        lines.append(self.upgrade_time_block())
        lines.append(self.cost_to_upgrade_block())
        lines.append(self.province_modifiers_block())
        lines.append(self.area_modifier_block())
        lines.append(self.region_modifier_block())
        lines.append(self.country_modifiers_block())
        lines.append(self.on_upgrade_block(self.on_upgrade))

        lines.append(f"{tab}}}")

        block = "\n".join(lines) + "\n"

        return block


def parse_paradox(lines):
    '''
    Parsing the paradox tree style data
    Args:
         lines: the lines at the file
    '''
    stack = [[]]

    for raw in lines:
        line = raw.split("#", 1)[0].strip()

        if not line:
            continue

        if line.endswith("{"):
            key = line[:-1].split("=")[0].strip()
            new_block = []
            stack[-1].append((key, new_block))
            stack.append(new_block)

        elif line == "}":
            stack.pop()

        elif "=" in line:
            key, value = map(str.strip, line.split("=", 1))
            
            if value.startswith("{") and value.endswith("}"):
                inner = value[1:-1].strip()

                if inner:
                    inner_lines = [inner]
                    parsed = parse_paradox(inner_lines)
                else:
                    parsed = []

                stack[-1].append((key, parsed))

            else:
                stack[-1].append((key, value))

    return stack[0]



def read_monuments(path = ruta):
    '''
    function that reads the file of monuments
    Args:
         path(string): path to the files
    Returns:
         monument_list(list): list of all the monument class nodes
    '''
    with open(path, "r") as fl:
        datas = parse_paradox(fl)
    
    monument_dict = {}

    for monument in datas:
        monument_dict[monument[0]] = Monument(monument[0], monument[1])

    return monument_dict


def output(monument_data, path = ruta):
    with open(path, "w") as fl:
        for monument_elem in monument_data:
            #print(monument_elem)
            content = monument_data[monument_elem].build_up_the_whole()
            fl.write(content + "\n")
    


def test():
    data = read_monuments()
    data["hagia_sophia"].name = "dasd"
    data["hagia_sophia"].tier_3_country_modifiers = [("sads", 0.1)]

    res = data["amsterdam_bourse"].build_up_the_whole()
    #print(data["amsterdam_bourse"].tier_2_region_modifier)
    print(res)

#test()

