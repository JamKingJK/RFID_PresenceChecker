-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Lis 2020, 00:14
-- Wersja serwera: 10.4.14-MariaDB
-- Wersja PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `presence_check`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `dataiczas`
--

CREATE TABLE `dataiczas` (
  `id_dic` int(11) NOT NULL,
  `dic_start` datetime NOT NULL,
  `dic_stop` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `dataiczas`
--

INSERT INTO `dataiczas` (`id_dic`, `dic_start`, `dic_stop`) VALUES
(1, '2020-11-12 08:00:00', '2020-11-12 08:45:00'),
(2, '2020-11-12 08:50:00', '2020-11-12 09:35:00'),
(3, '2020-11-12 09:40:00', '2020-11-12 10:25:00'),
(4, '2020-11-12 10:30:00', '2020-11-12 11:15:00');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `klasa`
--

CREATE TABLE `klasa` (
  `id_klasy` int(11) NOT NULL,
  `nazwa_klasy` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `klasa`
--

INSERT INTO `klasa` (`id_klasy`, `nazwa_klasy`) VALUES
(1, '1A'),
(2, '1B'),
(3, '2A'),
(4, '2B'),
(5, '3A'),
(6, '3B'),
(7, '3C'),
(8, '4A');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lekcja`
--

CREATE TABLE `lekcja` (
  `id_lekcji` int(11) NOT NULL,
  `id_przedmiotu_fk` int(11) NOT NULL,
  `id_dic_fk` int(11) NOT NULL,
  `id_klasy_fk` int(11) NOT NULL,
  `id_sali_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `lekcja`
--

INSERT INTO `lekcja` (`id_lekcji`, `id_przedmiotu_fk`, `id_dic_fk`, `id_klasy_fk`, `id_sali_fk`) VALUES
(1, 1, 1, 1, 1),
(2, 1, 1, 7, 7);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przedmiot`
--

CREATE TABLE `przedmiot` (
  `id_przedmiotu` int(11) NOT NULL,
  `nazwa_przedmiotu` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `przedmiot`
--

INSERT INTO `przedmiot` (`id_przedmiotu`, `nazwa_przedmiotu`) VALUES
(1, 'Język polski'),
(2, 'Matematyka'),
(3, 'Informatyka-specjalizacja'),
(4, 'Język angielski'),
(5, 'Projektowanie baz danych');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sala`
--

CREATE TABLE `sala` (
  `id_sali` int(11) NOT NULL,
  `numer_sali` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `sala`
--

INSERT INTO `sala` (`id_sali`, `numer_sali`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 101),
(5, 102),
(6, 103),
(7, 201),
(8, 202),
(9, 203),
(10, 301),
(11, 302),
(12, 303);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `uczen`
--

CREATE TABLE `uczen` (
  `id_ucznia` int(11) NOT NULL,
  `karta` int(11) NOT NULL,
  `imie` text COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` text COLLATE utf8_polish_ci NOT NULL,
  `id_klasy_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `uczen`
--

INSERT INTO `uczen` (`id_ucznia`, `karta`, `imie`, `nazwisko`, `id_klasy_fk`) VALUES
(1, 2137, 'Dawid', 'Kozieł', 1),
(2, 3692, 'Kacpur', 'Pągowski', 2),
(7, 1234, 'Elo', 'Benc', 2),
(8, 123456, 'Kacper', 'Cwel', 1),
(9, 2136, 'Maruś', 'Testowy', 5);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wpis`
--

CREATE TABLE `wpis` (
  `id_lekcji_fk` int(11) NOT NULL,
  `id_ucznia_fk` int(11) NOT NULL,
  `obecnosc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `wpis`
--

INSERT INTO `wpis` (`id_lekcji_fk`, `id_ucznia_fk`, `obecnosc`) VALUES
(1, 1, 1),
(1, 2, 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `dataiczas`
--
ALTER TABLE `dataiczas`
  ADD PRIMARY KEY (`id_dic`);

--
-- Indeksy dla tabeli `klasa`
--
ALTER TABLE `klasa`
  ADD PRIMARY KEY (`id_klasy`);

--
-- Indeksy dla tabeli `lekcja`
--
ALTER TABLE `lekcja`
  ADD PRIMARY KEY (`id_lekcji`),
  ADD KEY `klasa_keyL` (`id_klasy_fk`),
  ADD KEY `przedmiot_key` (`id_przedmiotu_fk`),
  ADD KEY `sala_key` (`id_sali_fk`),
  ADD KEY `dic_key` (`id_dic_fk`);

--
-- Indeksy dla tabeli `przedmiot`
--
ALTER TABLE `przedmiot`
  ADD PRIMARY KEY (`id_przedmiotu`);

--
-- Indeksy dla tabeli `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`id_sali`);

--
-- Indeksy dla tabeli `uczen`
--
ALTER TABLE `uczen`
  ADD PRIMARY KEY (`id_ucznia`),
  ADD KEY `id_klasy_keyU` (`id_klasy_fk`);

--
-- Indeksy dla tabeli `wpis`
--
ALTER TABLE `wpis`
  ADD KEY `id_ucznia_key` (`id_ucznia_fk`),
  ADD KEY `id_lekcji_key` (`id_lekcji_fk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `dataiczas`
--
ALTER TABLE `dataiczas`
  MODIFY `id_dic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT dla tabeli `klasa`
--
ALTER TABLE `klasa`
  MODIFY `id_klasy` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `lekcja`
--
ALTER TABLE `lekcja`
  MODIFY `id_lekcji` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT dla tabeli `przedmiot`
--
ALTER TABLE `przedmiot`
  MODIFY `id_przedmiotu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `sala`
--
ALTER TABLE `sala`
  MODIFY `id_sali` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `uczen`
--
ALTER TABLE `uczen`
  MODIFY `id_ucznia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `lekcja`
--
ALTER TABLE `lekcja`
  ADD CONSTRAINT `dic_key` FOREIGN KEY (`id_dic_fk`) REFERENCES `dataiczas` (`id_dic`) ON UPDATE CASCADE,
  ADD CONSTRAINT `klasa_keyL` FOREIGN KEY (`id_klasy_fk`) REFERENCES `klasa` (`id_klasy`) ON UPDATE CASCADE,
  ADD CONSTRAINT `przedmiot_key` FOREIGN KEY (`id_przedmiotu_fk`) REFERENCES `przedmiot` (`id_przedmiotu`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sala_key` FOREIGN KEY (`id_sali_fk`) REFERENCES `sala` (`id_sali`) ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `uczen`
--
ALTER TABLE `uczen`
  ADD CONSTRAINT `id_klasy_keyU` FOREIGN KEY (`id_klasy_fk`) REFERENCES `klasa` (`id_klasy`) ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `wpis`
--
ALTER TABLE `wpis`
  ADD CONSTRAINT `id_lekcji_key` FOREIGN KEY (`id_lekcji_fk`) REFERENCES `lekcja` (`id_lekcji`) ON UPDATE CASCADE,
  ADD CONSTRAINT `id_ucznia_key` FOREIGN KEY (`id_ucznia_fk`) REFERENCES `uczen` (`id_ucznia`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
