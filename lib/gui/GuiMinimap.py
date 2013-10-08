from GuiGroup import GuiGroup
from GuiColorRect import GuiColorRect
from State import State

class GuiMinimap(GuiGroup):
    def __init__(self,x,y,agents):
        GuiGroup.__init__(self,[],x,y,100,100)
        self.background_rect = GuiColorRect(0,0,self.width,self.height)
        self.background_rect.color = [0.0,0.0,0.0,0.33]
        self.objectList.append(self.background_rect)
        
        self.window_rect = GuiColorRect(2,2,4,4)
        self.window_rect.color = [1.0,0.0,0.0,0.5]
        self.objectList.append(self.window_rect)
        
        self.point_rect = GuiColorRect(((float(State().point.x) / State().game_size[0])-0.5)*self.width,((float(State().point.y) / State().game_size[1])-0.5)*self.height,4,4)
        self.point_rect.color = [0.0,1.0,0.0,0.5]
        self.objectList.append(self.point_rect)
        
        self.agents = {}
        for agent in agents:
            agent_rect = GuiColorRect(agent.x,agent.y,2,2)
            agent_rect.color = [1.0, 1.0, 1.0, 0.5]
            self.objectList.append(agent_rect)
            self.agents[agent] = agent_rect
        
        self.agents[State().hawk] = GuiColorRect(State().hawk.x,State().hawk.y,2,2)
        self.agents[State().hawk].color = [0.0,0.1,0.1,0.5]
        self.objectList.append(self.agents[State().hawk])
        
        for fire in State().fires:
            fire_rect = GuiColorRect(((float(fire.x) / State().game_size[0])-0.5)*self.width,((float(fire.y) / State().game_size[1])-0.5)*self.height,4,4)
            fire_rect.color = [1.0,0.5,0.0,0.75]
            self.objectList.append(fire_rect)
    
    def update(self):    
        self.window_rect.x = ((float(State().player.x) / State().game_size[0])-0.5)*self.width
        self.window_rect.y = ((float(State().player.y) / State().game_size[1])-0.5)*self.height
        
        dead_agents = []
        for agent,rect in self.agents.items():
            if agent.boidState == "Dead":
                dead_agents.append(agent)
            rect.x = ((float(agent.x) / State().game_size[0])-0.5)*self.width
            rect.y = ((float(agent.y) / State().game_size[1])-0.5)*self.height
            if agent.isCaptured:
                rect.color = [1.0,1.0,0.0,0.5]
        for agent in dead_agents:
            self.objectList.remove(self.agents[agent])
            del self.agents[agent]
        
        GuiGroup.update(self)