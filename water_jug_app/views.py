from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import water_jug_solver

class WaterJugView(APIView):
    def post(self, request):
        x_capacity = request.data.get('x_capacity')
        y_capacity = request.data.get('y_capacity')
        z_amount_wanted = request.data.get('z_amount_wanted')

        # Validate inputs
        if not all(isinstance(i, int) and i > 0 for i in [x_capacity, y_capacity, z_amount_wanted]):
            return Response({"error": "All inputs must be positive integers"}, status=status.HTTP_400_BAD_REQUEST)

        solution = water_jug_solver(x_capacity, y_capacity, z_amount_wanted)
        return Response(solution, status=status.HTTP_200_OK)
