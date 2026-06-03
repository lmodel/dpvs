---
search:
  boost: 10.0
---

# Class: TTPOS 


_Concept representing region Port of Spain in country Trinidad and Tobago_



<div data-search-exclude markdown="1">



URI: [loc:TT-POS](https://w3id.org/lmodel/dpv/loc/TT-POS)





```mermaid
 classDiagram
    class TTPOS
    click TTPOS href "../TTPOS/"
      TT <|-- TTPOS
        click TT href "../TT/"
      
      
```





## Inheritance
* [TT](TT.md)
    * **TTPOS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TT-POS](https://w3id.org/lmodel/dpv/loc/TT-POS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TT-POS
* Port of Spain




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TT-POS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TT-POS |
| native | loc:TTPOS |
| exact | dpv_loc:TT-POS, dpv_loc_owl:TT-POS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TTPOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TT-POS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port of Spain in country Trinidad and Tobago
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TT-POS
- Port of Spain
exact_mappings:
- dpv_loc:TT-POS
- dpv_loc_owl:TT-POS
is_a: TT
class_uri: loc:TT-POS

```
</details>

### Induced

<details>
```yaml
name: TTPOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TT-POS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port of Spain in country Trinidad and Tobago
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TT-POS
- Port of Spain
exact_mappings:
- dpv_loc:TT-POS
- dpv_loc_owl:TT-POS
is_a: TT
class_uri: loc:TT-POS

```
</details></div>