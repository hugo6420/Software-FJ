from excepciones.excepciones import (
    ClienteDuplicadoError,
    ServicioDuplicadoError,
    ReservaDuplicadaError,
    ValidacionError
)


class SistemaSoftwareFJ:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # ---------------- CLIENTES ----------------

    def agregar_cliente(self, cliente):

        for c in self.clientes:

            if c.codigo == cliente.codigo:
                raise ClienteDuplicadoError(
                    "Cliente repetido."
                )

        self.clientes.append(cliente)

    def buscar_cliente(self, codigo):

        for cliente in self.clientes:

            if cliente.codigo == codigo:

                return cliente

        raise ValidacionError(
            "Cliente no encontrado."
        )

    def mostrar_clientes(self):

        print("\n===== CLIENTES =====\n")

        for cliente in self.clientes:

            print(cliente.mostrar())
            print("-" * 40)

    # ---------------- SERVICIOS ----------------

    def agregar_servicio(self, servicio):

        for s in self.servicios:

            if s.codigo == servicio.codigo:

                raise ServicioDuplicadoError(
                    "Servicio repetido."
                )

        self.servicios.append(servicio)

    def buscar_servicio(self, codigo):

        for servicio in self.servicios:

            if servicio.codigo == codigo:

                return servicio

        raise ValidacionError(
            "Servicio no encontrado."
        )

    def mostrar_servicios(self):

        print("\n===== SERVICIOS =====\n")

        for servicio in self.servicios:

            print(servicio.mostrar())
            print(servicio.descripcion())
            print("-" * 40)

    # ---------------- RESERVAS ----------------

    def agregar_reserva(self, reserva):

        for r in self.reservas:

            if r.codigo == reserva.codigo:

                raise ReservaDuplicadaError(
                    "Reserva repetida."
                )

        self.reservas.append(reserva)

    def mostrar_reservas(self):

        print("\n===== RESERVAS =====\n")

        for reserva in self.reservas:

            print(reserva.mostrar())
            print("-" * 40)

    # ---------------- POLIMORFISMO ----------------

    def mostrar_costos(self):

        print("\n===== COSTOS =====\n")

        for servicio in self.servicios:

            print(servicio.nombre)
            print(servicio.descripcion())
            print(
                f"Costo: ${servicio.calcular_costo(2):,.0f}"
            )
            print("-" * 40)

    # ---------------- RESUMEN ----------------

    def resumen(self):

        print("\n========= RESUMEN =========")

        print(f"Clientes : {len(self.clientes)}")
        print(f"Servicios : {len(self.servicios)}")
        print(f"Reservas : {len(self.reservas)}")