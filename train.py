import retro

def main():
    env = retro.make(game="MarioDuck", obs_type=retro.Observations.RAM)
    state = env.reset()
    print(state)
    print(env.action_space.shape)
    print(env.observation_space.shape)
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()
    env.close()

if __name__ == "__main__":
    main()
