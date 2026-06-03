---
search:
  boost: 10.0
---

# Class: SVUN 


_Concept representing region La Unión Department in country El Salvador_



<div data-search-exclude markdown="1">



URI: [loc:SV-UN](https://w3id.org/lmodel/dpv/loc/SV-UN)





```mermaid
 classDiagram
    class SVUN
    click SVUN href "../SVUN/"
      SV <|-- SVUN
        click SV href "../SV/"
      
      
```





## Inheritance
* [SV](SV.md)
    * **SVUN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SV-UN](https://w3id.org/lmodel/dpv/loc/SV-UN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SV-UN
* La Unión Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SV-UN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SV-UN |
| native | loc:SVUN |
| exact | dpv_loc:SV-UN, dpv_loc_owl:SV-UN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SVUN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SV-UN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region La Unión Department in country El Salvador
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SV-UN
- La Unión Department
exact_mappings:
- dpv_loc:SV-UN
- dpv_loc_owl:SV-UN
is_a: SV
class_uri: loc:SV-UN

```
</details>

### Induced

<details>
```yaml
name: SVUN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SV-UN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region La Unión Department in country El Salvador
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SV-UN
- La Unión Department
exact_mappings:
- dpv_loc:SV-UN
- dpv_loc_owl:SV-UN
is_a: SV
class_uri: loc:SV-UN

```
</details></div>