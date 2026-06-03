---
search:
  boost: 10.0
---

# Class: DpvIdentifier 


_Information about an identifier or name used for identification_



<div data-search-exclude markdown="1">



URI: [pd:Identifier](https://w3id.org/lmodel/dpv/pd/Identifier)





```mermaid
 classDiagram
    class DpvIdentifier
    click DpvIdentifier href "../DpvIdentifier/"
      Tracking <|-- DpvIdentifier
        click Tracking href "../Tracking/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * **DpvIdentifier**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Identifier](https://w3id.org/lmodel/dpv/pd/Identifier) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Identifier




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Identifier |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Identifier |
| native | pd:DpvIdentifier |
| exact | dpv_pd:Identifier, dpv_pd_owl:Identifier |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvIdentifier
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Identifier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an identifier or name used for identification
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Identifier
exact_mappings:
- dpv_pd:Identifier
- dpv_pd_owl:Identifier
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Tracking
class_uri: pd:Identifier

```
</details>

### Induced

<details>
```yaml
name: DpvIdentifier
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Identifier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an identifier or name used for identification
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Identifier
exact_mappings:
- dpv_pd:Identifier
- dpv_pd_owl:Identifier
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Tracking
class_uri: pd:Identifier

```
</details></div>