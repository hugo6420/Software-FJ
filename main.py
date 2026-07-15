from modelos.cliente import Cliente
from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria
from modelos.reserva import Reserva

from sistema.sistema import SistemaSoftwareFJ


def cargar_datos(sistema):

    sistema.agregar_cliente(
        Cliente(
            "1001",
            "Juan Perez",
            "juan@gmail.com",
            "3101111111"
        )
    )

    sistema.agregar_cliente(
        Cliente(
            "1002",
            "Maria Lopez",
            "maria@gmail.com",
            "3202222222"
        )
    )

    sistema.agregar_servicio(
        Sala(
            "S01",
            "Sala Ejecutiva",
            60000,
            20
        )
    )

    sistema.agregar_servicio(
        Equipo(
            "E01",
            "Video Beam",
            90000,
            "Multimedia"
        )
    )

    sistema.agregar_servicio(
        Asesoria(
            "A01",
            "Python",
            120000,
            "Ingeniero Senior"
        )
    )
def simulacion(sistema):

    print("\n========== SIMULACIÓN ==========\n")

    print("1. Cliente duplicado")

    try:
        sistema.agregar_cliente(
            Cliente(
                "1001",
                "Pedro Perez",
                "pedro@gmail.com",
                "3100000000"
            )
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n2. Buscar cliente inexistente")

    try:
        sistema.buscar_cliente("9999")

    except Exception as e:
        print("Error controlado:", e)

    print("\n3. Buscar servicio inexistente")

    try:
        sistema.buscar_servicio("XXX")

    except Exception as e:
        print("Error controlado:", e)

    print("\n4. Confirmar reserva")

    try:

        reserva = sistema.reservas[0]

        reserva.confirmar()

        print("Estado:", reserva.estado)

    except Exception as e:

        print("Error:", e)

    print("\n5. Confirmar nuevamente la misma reserva")

    try:

        reserva.confirmar()

    except Exception as e:

        print("Error controlado:", e)

    print("\n========== FIN DE LA SIMULACIÓN ==========")

def main():

    sistema = SistemaSoftwareFJ()

    cargar_datos(sistema)

    reserva = Reserva(
        "R001",
        sistema.buscar_cliente("1001"),
        sistema.buscar_servicio("S01"),
        2
    )

    sistema.agregar_reserva(reserva)

    while True:

        print("\n===== SOFTWARE FJ =====")
        print("1. Clientes")
        print("2. Servicios")
        print("3. Reservas")
        print("4. Costos")
        print("5. Resumen")
        print("6. Ejecutar simulación")
        print("0. Salir")

        opcion = input("\nSeleccione: ")

        if opcion == "1":
            sistema.mostrar_clientes()

        elif opcion == "2":
            sistema.mostrar_servicios()

        elif opcion == "3":
            sistema.mostrar_reservas()

        elif opcion == "4":
            sistema.mostrar_costos()

        elif opcion == "5":
            sistema.resumen()

        elif opcion == "6":
            simulacion(sistema)

        elif opcion == "0":
            print("\nHasta luego.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()

    