---
search:
  boost: 10.0
---

# Class: ARC 


_Concept representing region Buenos Aires in country Argentina_



<div data-search-exclude markdown="1">



URI: [loc:AR-C](https://w3id.org/lmodel/dpv/loc/AR-C)





```mermaid
 classDiagram
    class ARC
    click ARC href "../ARC/"
      AR <|-- ARC
        click AR href "../AR/"
      
      
```





## Inheritance
* [AR](AR.md)
    * **ARC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AR-C](https://w3id.org/lmodel/dpv/loc/AR-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AR-C
* Buenos Aires




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AR-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AR-C |
| native | loc:ARC |
| exact | dpv_loc:AR-C, dpv_loc_owl:AR-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ARC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Buenos Aires in country Argentina
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AR-C
- Buenos Aires
exact_mappings:
- dpv_loc:AR-C
- dpv_loc_owl:AR-C
is_a: AR
class_uri: loc:AR-C

```
</details>

### Induced

<details>
```yaml
name: ARC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Buenos Aires in country Argentina
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AR-C
- Buenos Aires
exact_mappings:
- dpv_loc:AR-C
- dpv_loc_owl:AR-C
is_a: AR
class_uri: loc:AR-C

```
</details></div>