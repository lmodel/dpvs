---
search:
  boost: 10.0
---

# Class: TVViewingBehaviour 


_Information about TV viewing behaviour, such as timestamps of channel_

_change, duration of viewership, content consumed_



<div data-search-exclude markdown="1">



URI: [pd:TVViewingBehaviour](https://w3id.org/lmodel/dpv/pd/TVViewingBehaviour)





```mermaid
 classDiagram
    class TVViewingBehaviour
    click TVViewingBehaviour href "../TVViewingBehaviour/"
      ServiceConsumptionBehaviour <|-- TVViewingBehaviour
        click ServiceConsumptionBehaviour href "../ServiceConsumptionBehaviour/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * [ServiceConsumptionBehaviour](ServiceConsumptionBehaviour.md)
            * **TVViewingBehaviour**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:TVViewingBehaviour](https://w3id.org/lmodel/dpv/pd/TVViewingBehaviour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* TV Viewing Behaviour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#TVViewingBehaviour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:TVViewingBehaviour |
| native | pd:TVViewingBehaviour |
| exact | dpv_pd:TVViewingBehaviour, dpv_pd_owl:TVViewingBehaviour |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TVViewingBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TVViewingBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about TV viewing behaviour, such as timestamps of channel

  change, duration of viewership, content consumed'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- TV Viewing Behaviour
exact_mappings:
- dpv_pd:TVViewingBehaviour
- dpv_pd_owl:TVViewingBehaviour
is_a: ServiceConsumptionBehaviour
class_uri: pd:TVViewingBehaviour

```
</details>

### Induced

<details>
```yaml
name: TVViewingBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TVViewingBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about TV viewing behaviour, such as timestamps of channel

  change, duration of viewership, content consumed'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- TV Viewing Behaviour
exact_mappings:
- dpv_pd:TVViewingBehaviour
- dpv_pd_owl:TVViewingBehaviour
is_a: ServiceConsumptionBehaviour
class_uri: pd:TVViewingBehaviour

```
</details></div>