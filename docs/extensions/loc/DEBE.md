---
search:
  boost: 10.0
---

# Class: DEBE 


_Concept representing region Berlin in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-BE](https://w3id.org/lmodel/dpv/loc/DE-BE)





```mermaid
 classDiagram
    class DEBE
    click DEBE href "../DEBE/"
      DE <|-- DEBE
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEBE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-BE](https://w3id.org/lmodel/dpv/loc/DE-BE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-BE
* Berlin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-BE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-BE |
| native | loc:DEBE |
| exact | dpv_loc:DE-BE, dpv_loc_owl:DE-BE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEBE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Berlin in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BE
- Berlin
exact_mappings:
- dpv_loc:DE-BE
- dpv_loc_owl:DE-BE
is_a: DE
class_uri: loc:DE-BE

```
</details>

### Induced

<details>
```yaml
name: DEBE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Berlin in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BE
- Berlin
exact_mappings:
- dpv_loc:DE-BE
- dpv_loc_owl:DE-BE
is_a: DE
class_uri: loc:DE-BE

```
</details></div>