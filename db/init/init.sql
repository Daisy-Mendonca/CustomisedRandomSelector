--
-- PostgreSQL database dump
--

\restrict 6K1hSzMl5Wqxfm4DpHAZeCuinANbFdlSfPO8bvpn2SfIEhMskQFa6XvRS886cvF

-- Dumped from database version 18.1 (Postgres.app)
-- Dumped by pg_dump version 18.1 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: foodcategory; Type: TYPE; Schema: public; Owner: daisy
--

CREATE TYPE public.foodcategory AS ENUM (
    'Breakfast',
    'Meal'
);


ALTER TYPE public.foodcategory OWNER TO daisy;

--
-- Name: foodtype; Type: TYPE; Schema: public; Owner: daisy
--

CREATE TYPE public.foodtype AS ENUM (
    'NA',
    'Veg',
    'Non_Veg'
);


ALTER TYPE public.foodtype OWNER TO daisy;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: food_items; Type: TABLE; Schema: public; Owner: daisy
--

CREATE TABLE public.food_items (
    id integer NOT NULL,
    name character varying NOT NULL,
    category public.foodcategory NOT NULL,
    type public.foodtype NOT NULL,
    last_used timestamp with time zone
);


ALTER TABLE public.food_items OWNER TO daisy;

--
-- Name: food_items_id_seq; Type: SEQUENCE; Schema: public; Owner: daisy
--

CREATE SEQUENCE public.food_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.food_items_id_seq OWNER TO daisy;

--
-- Name: food_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: daisy
--

ALTER SEQUENCE public.food_items_id_seq OWNED BY public.food_items.id;


--
-- Name: food_items id; Type: DEFAULT; Schema: public; Owner: daisy
--

ALTER TABLE ONLY public.food_items ALTER COLUMN id SET DEFAULT nextval('public.food_items_id_seq'::regclass);


--
-- Data for Name: food_items; Type: TABLE DATA; Schema: public; Owner: daisy
--

COPY public.food_items (id, name, category, type, last_used) FROM stdin;
2	Oats	Breakfast	NA	2025-12-09 00:00:00+01
3	Bread peanut butter	Breakfast	NA	2025-12-09 00:00:00+01
5	Ragi malt	Breakfast	NA	2025-12-09 00:00:00+01
7	Upma	Breakfast	NA	2025-12-09 00:00:00+01
8	Vermicelli	Breakfast	NA	2025-12-09 00:00:00+01
10	Sajjige Bajil	Breakfast	NA	2025-12-09 00:00:00+01
11	Ganji	Meal	Veg	2025-12-09 00:00:00+01
12	Biryani	Meal	Non_Veg	2025-12-09 00:00:00+01
13	Dal-palak	Meal	Veg	2025-12-09 00:00:00+01
14	Dal fry	Meal	Veg	2025-12-09 00:00:00+01
15	Tomato Rasam	Meal	Veg	2025-12-09 00:00:00+01
17	Veg pulav	Meal	Veg	2025-12-09 00:00:00+01
18	Chicken pulav	Meal	Non_Veg	2025-12-09 00:00:00+01
19	Chana masala	Meal	Veg	2025-12-09 00:00:00+01
20	Moong curry	Meal	Veg	2025-12-09 00:00:00+01
21	Lentil curry	Meal	Veg	2025-12-09 00:00:00+01
22	Green chicken curry	Meal	Non_Veg	2025-12-09 00:00:00+01
23	Chicken normal curry	Meal	Non_Veg	2025-12-09 00:00:00+01
24	Chicken coconut curry	Meal	Non_Veg	2025-12-09 00:00:00+01
25	Chicken sukka	Meal	Non_Veg	2025-12-09 00:00:00+01
26	Sambhar	Meal	Veg	2025-12-09 00:00:00+01
27	Fried rice	Meal	Non_Veg	2025-12-09 00:00:00+01
28	Puliyoggare	Meal	Veg	2025-12-09 00:00:00+01
29	Lemon rice	Meal	Veg	2025-12-09 00:00:00+01
30	Thai curry	Meal	Non_Veg	2025-12-09 00:00:00+01
31	Beans 	Meal	Veg	2025-12-09 00:00:00+01
32	Beetroot	Meal	Veg	2025-12-09 00:00:00+01
33	Chapati baji	Meal	Veg	2025-12-09 00:00:00+01
34	Egg rice	Meal	Non_Veg	2025-12-09 00:00:00+01
35	Ragi dosa	Meal	Veg	2025-12-09 00:00:00+01
36	Rava idli	Meal	Veg	2025-12-09 00:00:00+01
37	Dosa	Meal	Veg	2025-12-09 00:00:00+01
38	Normal idli	Meal	Veg	2025-12-09 00:00:00+01
39	Curd rice 	Meal	Veg	2025-12-09 00:00:00+01
40	Pepper chicken	Meal	Non_Veg	2025-12-09 00:00:00+01
41	Pasta	Meal	Veg	2025-12-09 00:00:00+01
9	Brezel	Breakfast	NA	2025-12-15 15:00:03.617918+01
42	Egg curry	Meal	Non_Veg	2025-12-15 15:49:14.700093+01
6	Poha	Breakfast	NA	2025-12-16 16:11:34.04949+01
1	Avocado toast	Breakfast	NA	2025-12-16 16:12:44.146361+01
16	Rajma chawal	Meal	Veg	2025-12-16 16:20:49.319051+01
4	Bread cheese veg sandwich	Breakfast	NA	2025-12-16 16:20:59.431132+01
\.


--
-- Name: food_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: daisy
--

SELECT pg_catalog.setval('public.food_items_id_seq', 42, true);


--
-- Name: food_items food_items_pkey; Type: CONSTRAINT; Schema: public; Owner: daisy
--

ALTER TABLE ONLY public.food_items
    ADD CONSTRAINT food_items_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict 6K1hSzMl5Wqxfm4DpHAZeCuinANbFdlSfPO8bvpn2SfIEhMskQFa6XvRS886cvF

