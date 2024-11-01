import rlcard  # Importem dos mòduls del "paquet" rlcard.
from rlcard.agents import DQNAgent  # Aquí importem una classe que implementa un algorisme Deep-Q.
from rlcard.utils import (
    tournament,  # Manera en la qual l’agent s’entrenarà.
    reorganize,  # Reorganitzar les dades d’una manera òptima per elaborar gràfics.
    Logger,  # Una classe per acumular informació durant l’entrenament.
    plot_curve,  # Una funció per determinar la corva d’aprenentatge.
)

# Creem una instància de l’entorn del blackjack utilitzant el mètode make().
entorn = rlcard.make("blackjack")

# Creem una instància de la classe DQNAgent
agent = DQNAgent(
    num_actions=entorn.num_actions,  # Nombre d’accions que es poden prendre
    state_shape=entorn.state_shape[0],  # Forma de l’estat representat (vector unidimensional)
    mlp_layers=[64, 64],  # Nombre de neurons a cada capa de la xarxa neuronal.
)

# L’agent creat abans és l’únic a l’entorn.
entorn.set_agents([agent])

# Creem un Logger per emmagatzemar el rendiment durant l’entrenament.
with Logger("experiments/leduc_holdem_dqn_result/") as logger:
    for episode in range(1000):  # El bucle d’entrenament serà de 1000 episodis.
        # Per a cada episodi, les trajectòries i pagaments de l’entorn es graven.
        trajectories, payoffs = entorn.run(is_training=True)

        # Les trajectòries es reorganitzen per a la màxima eficiència durant l’entrenament i l’agent reb els resultats.
        trajectories = reorganize(trajectories, payoffs)
        for ts in trajectories[0]:
            agent.feed(ts)

        # Per a cada 50 episodis, el rendiment de l'agent es guarda.
        if episode % 50 == 0:
            logger.log_performance(
                entorn.timestep,
                tournament(entorn, 10000)[0]
            )

    # El lloc en el qual s’envien les dades.
    csv_path, fig_path = logger.csv_path, logger.fig_path

    # Es representa gràficament l’evolució de l’estil de joc de l'agent.
    plot_curve(csv_path, fig_path, "DQN")
