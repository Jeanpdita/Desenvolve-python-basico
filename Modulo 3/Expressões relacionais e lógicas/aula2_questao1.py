{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gu4kTwDZCAcJ",
        "outputId": "bbb18927-047e-413d-de08-98482810b3c9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a idade de Juliana: 16\n",
            "Digite a idade de Cris: 17\n",
            "False\n",
            "Juliana e Cris não podem entrar no bar.\n"
          ]
        }
      ],
      "source": [
        "#  entrada\n",
        "idade_juliana = int(input(\"Digite a idade de Juliana: \"))\n",
        "idade_cris = int(input(\"Digite a idade de Cris: \"))\n",
        "\n",
        "# processando\n",
        "podem_entrar = idade_juliana > 17 and idade_cris > 17\n",
        "\n",
        "# saida\n",
        "if podem_entrar:\n",
        "    print(True)\n",
        "else:\n",
        "    print(False)\n",
        "    print(\"Juliana e Cris não podem entrar no bar.\")"
      ]
    }
  ]
}