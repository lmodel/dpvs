---
search:
  boost: 10.0
---

# Class: CODC 


_Concept representing region Bogotá in country Colombia_



<div data-search-exclude markdown="1">



URI: [loc:CO-DC](https://w3id.org/lmodel/dpv/loc/CO-DC)





```mermaid
 classDiagram
    class CODC
    click CODC href "../CODC/"
      CO <|-- CODC
        click CO href "../CO/"
      
      
```





## Inheritance
* [CO](CO.md)
    * **CODC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CO-DC](https://w3id.org/lmodel/dpv/loc/CO-DC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CO-DC
* Bogotá




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CO-DC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CO-DC |
| native | loc:CODC |
| exact | dpv_loc:CO-DC, dpv_loc_owl:CO-DC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CODC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-DC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bogotá in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-DC
- Bogotá
exact_mappings:
- dpv_loc:CO-DC
- dpv_loc_owl:CO-DC
is_a: CO
class_uri: loc:CO-DC

```
</details>

### Induced

<details>
```yaml
name: CODC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-DC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bogotá in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-DC
- Bogotá
exact_mappings:
- dpv_loc:CO-DC
- dpv_loc_owl:CO-DC
is_a: CO
class_uri: loc:CO-DC

```
</details></div>