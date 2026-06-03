---
search:
  boost: 10.0
---

# Class: MHARN 


_Concept representing region Arno Atoll in country Marshall Islands_



<div data-search-exclude markdown="1">



URI: [loc:MH-ARN](https://w3id.org/lmodel/dpv/loc/MH-ARN)





```mermaid
 classDiagram
    class MHARN
    click MHARN href "../MHARN/"
      MH <|-- MHARN
        click MH href "../MH/"
      
      
```





## Inheritance
* [MH](MH.md)
    * **MHARN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MH-ARN](https://w3id.org/lmodel/dpv/loc/MH-ARN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MH-ARN
* Arno Atoll




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MH-ARN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MH-ARN |
| native | loc:MHARN |
| exact | dpv_loc:MH-ARN, dpv_loc_owl:MH-ARN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MHARN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MH-ARN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arno Atoll in country Marshall Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MH-ARN
- Arno Atoll
exact_mappings:
- dpv_loc:MH-ARN
- dpv_loc_owl:MH-ARN
is_a: MH
class_uri: loc:MH-ARN

```
</details>

### Induced

<details>
```yaml
name: MHARN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MH-ARN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arno Atoll in country Marshall Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MH-ARN
- Arno Atoll
exact_mappings:
- dpv_loc:MH-ARN
- dpv_loc_owl:MH-ARN
is_a: MH
class_uri: loc:MH-ARN

```
</details></div>