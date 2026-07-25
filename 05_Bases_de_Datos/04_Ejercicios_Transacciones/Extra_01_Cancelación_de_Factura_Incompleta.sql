SET search_path TO "Ejercicios_Transactions";

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_invoice_number VARCHAR(15) := 'INV-202607-1004';
	v_bill_id INTEGER;
	v_current_status VARCHAR(10);
    v_product_not_delivered_01_id INTEGER := 8;
	v_product_not_delivered_02_id INTEGER := 9;
	v_delivered BOOLEAN;
	v_quantity INTEGER;

BEGIN
    -- 1. Verificar que la factura existe en la base de datos y está en estado "Pendiente".
	SELECT id INTO v_bill_id
	FROM bills
	WHERE invoice_number = v_invoice_number;

	IF v_bill_id IS NULL THEN
	  RAISE EXCEPTION 'La factura no existe en la base de datos';
	END IF;

	SELECT status INTO v_current_status
	FROM bills
	WHERE id = v_bill_id;

	IF v_current_status IS NULL OR v_current_status != 'Pendiente' THEN
	  RAISE EXCEPTION 'La factura no se encuentra en estado: Pendiente';
	END IF;

	--2. Cambiar su estado a "Cancelada".
	UPDATE bills
	SET status = 'Cancelada'
	WHERE id = v_bill_id;

	-- 3. Regresar el stock de los productos que aún no han sido entregados.
	-- Primer producto:
	SELECT delivered INTO v_delivered
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	  AND product_id = v_product_not_delivered_01_id;

	IF v_delivered IS NULL THEN
	  RAISE EXCEPTION 'El producto no estaba incluido en la compra';
	END IF;

	IF v_delivered THEN
	  RAISE EXCEPTION 'El producto ya fue entregado';
	END IF;

	SELECT quantity INTO v_quantity
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	  AND product_id = v_product_not_delivered_01_id;
	  
	UPDATE products
	SET stock = stock + v_quantity
	WHERE id = v_product_not_delivered_01_id;

	-- Segundo producto:
	SELECT delivered INTO v_delivered
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	  AND product_id = v_product_not_delivered_02_id;

	IF v_delivered IS NULL THEN
	  RAISE EXCEPTION 'El producto no estaba incluido en la compra';
	END IF;

	IF v_delivered THEN
	  RAISE EXCEPTION 'El producto ya fue entregado';
	END IF;

	SELECT quantity INTO v_quantity
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	  AND product_id = v_product_not_delivered_02_id;
	  
	UPDATE products
	SET stock = stock + v_quantity
	WHERE id = v_product_not_delivered_02_id;
	
	RAISE NOTICE 'Transacción exitosa. Los productos fueron regresados';
END $$;