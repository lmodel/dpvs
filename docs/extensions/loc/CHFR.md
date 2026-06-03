---
search:
  boost: 10.0
---

# Class: CHFR 


_Concept representing region Canton of Fribourg in country Switzerland_



<div data-search-exclude markdown="1">



URI: [loc:CH-FR](https://w3id.org/lmodel/dpv/loc/CH-FR)





```mermaid
 classDiagram
    class CHFR
    click CHFR href "../CHFR/"
      CH <|-- CHFR
        click CH href "../CH/"
      
      
```





## Inheritance
* [CH](CH.md)
    * **CHFR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CH-FR](https://w3id.org/lmodel/dpv/loc/CH-FR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CH-FR
* Canton of Fribourg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CH-FR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CH-FR |
| native | loc:CHFR |
| exact | dpv_loc:CH-FR, dpv_loc_owl:CH-FR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CHFR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CH-FR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Fribourg in country Switzerland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CH-FR
- Canton of Fribourg
exact_mappings:
- dpv_loc:CH-FR
- dpv_loc_owl:CH-FR
is_a: CH
class_uri: loc:CH-FR

```
</details>

### Induced

<details>
```yaml
name: CHFR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CH-FR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Fribourg in country Switzerland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CH-FR
- Canton of Fribourg
exact_mappings:
- dpv_loc:CH-FR
- dpv_loc_owl:CH-FR
is_a: CH
class_uri: loc:CH-FR

```
</details></div>