---
search:
  boost: 10.0
---

# Class: BQ 


_Concept representing Country of Bonaire, Sint Eustatius and Saba_



<div data-search-exclude markdown="1">



URI: [loc:BQ](https://w3id.org/lmodel/dpv/loc/BQ)





```mermaid
 classDiagram
    class BQ
    click BQ href "../BQ/"
      NL <|-- BQ
        click NL href "../NL/"
      

      BQ <|-- BQSE
        click BQSE href "../BQSE/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BQ**
            * [BQSE](BQSE.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BQ](https://w3id.org/lmodel/dpv/loc/BQ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Bonaire, Sint Eustatius and Saba




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BQ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BQ |
| native | loc:BQ |
| exact | dpv_loc:BQ, dpv_loc_owl:BQ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Bonaire, Sint Eustatius and Saba
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Bonaire, Sint Eustatius and Saba
exact_mappings:
- dpv_loc:BQ
- dpv_loc_owl:BQ
is_a: NL
class_uri: loc:BQ

```
</details>

### Induced

<details>
```yaml
name: BQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Bonaire, Sint Eustatius and Saba
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Bonaire, Sint Eustatius and Saba
exact_mappings:
- dpv_loc:BQ
- dpv_loc_owl:BQ
is_a: NL
class_uri: loc:BQ

```
</details></div>