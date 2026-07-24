SET search_path TO "Ejercicios_Transactions";

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_invoice_number VARCHAR(15) := 'INV-202607-1001';
	v_bill_id INTEGER;
    v_returned_product_id INTEGER := 7;
	v_quantity INTEGER;

BEGIN
    -- 1. Verificar que la factura existe en la base de datos.
	SELECT id INTO v_bill_id
	FROM bills
	WHERE invoice_number = v_invoice_number;

	IF v_bill_id IS NULL THEN
	  RAISE EXCEPTION 'La factura no existe en la base de datos';
	END IF;

	-- 2. Aumentar el stock de los productos en la cantidad que se registró en la compra.
	SELECT quantity INTO v_quantity
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	  AND product_id = v_returned_product_id;

	IF v_quantity IS NULL THEN
	  RAISE EXCEPTION 'El producto no estaba incluido en la compra';
	END IF;
	  
	UPDATE products
	SET stock = stock + v_quantity
	WHERE id = v_returned_product_id;

	--3. Modificar la factura original para marcarla con el estado de "Retornada".
	UPDATE bills
	SET status = 'Retornada'
	WHERE id = v_bill_id;
	
	RAISE NOTICE 'Transacción finalizada.';
END $$;